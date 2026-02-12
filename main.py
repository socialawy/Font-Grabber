"""
Font Grabber - Main GUI Application
"""
import customtkinter as ctk
from pathlib import Path
import threading
from tkinter import filedialog, messagebox
from core import FontManager
from config import Config


class FontGrabber(ctk.CTk):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        
        # Initialize config and manager
        self.config = Config()
        self.manager = FontManager(self.config.output_dir, self.config)
        
        # Setup window
        self.title("Font Grabber")
        self.geometry(self.config.get("window_size", "600x500"))
        
        # Set theme
        ctk.set_appearance_mode(self.config.get("theme", "dark"))
        ctk.set_default_color_theme("blue")
        
        # Track current search results
        self.current_results = {}
        
        # Build UI
        self._build_ui()
    
    def _build_ui(self):
        """Build the user interface."""
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # ===== HEADER =====
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="Font Grabber",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(side="left")
        
        # Settings button
        settings_btn = ctk.CTkButton(
            header_frame,
            text="⚙",
            width=40,
            command=self._open_settings
        )
        settings_btn.pack(side="right")
        
        # ===== SEARCH BAR =====
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)
        search_frame.grid_columnconfigure(0, weight=1)
        
        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(
            search_frame,
            textvariable=self.search_var,
            placeholder_text="Enter font name (e.g., Roboto, Inter, Montserrat)...",
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.search_entry.bind("<Return>", lambda e: self._search())
        
        self.search_btn = ctk.CTkButton(
            search_frame,
            text="Search",
            width=100,
            height=40,
            command=self._search,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.search_btn.grid(row=0, column=1)
        
        # ===== STATUS BAR =====
        self.status_label = ctk.CTkLabel(
            self,
            text=f"Ready | Output: {self.config.output_dir}",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        self.status_label.grid(row=3, column=0, sticky="ew", padx=20, pady=(5, 10))
        
        # ===== RESULTS FRAME =====
        self.results_frame = ctk.CTkScrollableFrame(self)
        self.results_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)
        
        # Initial message
        self._show_welcome_message()
    
    def _show_welcome_message(self):
        """Display welcome message in results area."""
        welcome = ctk.CTkLabel(
            self.results_frame,
            text="🔍 Search for fonts from Google Fonts\n\n"
                 "Type a font name and press Search or Enter",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        welcome.pack(pady=50)
    
    def _clear_results(self):
        """Clear the results frame."""
        for widget in self.results_frame.winfo_children():
            widget.destroy()
    
    def _update_status(self, message: str, color: str = "gray"):
        """Update status bar."""
        self.status_label.configure(text=message, text_color=color)
    
    def _search(self):
        """Perform font search."""
        query = self.search_var.get().strip()
        
        if not query:
            messagebox.showwarning("Empty Search", "Please enter a font name")
            return
        
        # Disable search while processing
        self.search_btn.configure(state="disabled", text="Searching...")
        self._update_status(f"Searching for '{query}'...", "orange")
        
        # Search in background thread
        def search_thread():
            try:
                results = self.manager.search(query)
                self.after(0, lambda: self._display_results(query, results))
            except Exception as e:
                self.after(0, lambda: self._search_error(str(e)))
        
        threading.Thread(target=search_thread, daemon=True).start()
    
    def _search_error(self, error: str):
        """Handle search error."""
        self.search_btn.configure(state="normal", text="Search")
        self._update_status(f"Error: {error}", "red")
        messagebox.showerror("Search Error", f"Failed to search:\n{error}")
    
    def _display_results(self, query: str, results: dict):
        """Display search results."""
        self.search_btn.configure(state="normal", text="Search")
        self._clear_results()
        
        if not results:
            self._update_status(f"No results found for '{query}'", "orange")
            no_results = ctk.CTkLabel(
                self.results_frame,
                text=f"😕 No fonts found matching '{query}'\n\n"
                     "Try a different name or check your spelling",
                font=ctk.CTkFont(size=14),
                text_color="orange"
            )
            no_results.pack(pady=50)
            return
        
        self.current_results = results
        total_matches = sum(len(fonts) for fonts in results.values())
        self._update_status(f"Found {total_matches} matches for '{query}'", "green")
        
        # Display results by source
        for source_name, fonts in results.items():
            # Source header
            source_header = ctk.CTkLabel(
                self.results_frame,
                text=f"📚 {source_name} ({len(fonts)} results)",
                font=ctk.CTkFont(size=16, weight="bold"),
                anchor="w"
            )
            source_header.pack(fill="x", pady=(10, 5), padx=5)
            
            # Font cards
            for font in fonts:
                self._create_font_card(source_name, font)
    
    def _create_font_card(self, source_name: str, font: dict):
        """Create a card for a single font result."""
        card = ctk.CTkFrame(self.results_frame)
        card.pack(fill="x", pady=5, padx=5)
        
        # Left side: Font info
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=15, pady=10)
        
        # Font name
        name_label = ctk.CTkLabel(
            info_frame,
            text=font["name"],
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        # Variants
        variants_text = f"{len(font['variants'])} variants: {', '.join(font['variants'][:3])}"
        if len(font['variants']) > 3:
            variants_text += "..."
        
        variants_label = ctk.CTkLabel(
            info_frame,
            text=variants_text,
            font=ctk.CTkFont(size=12),
            text_color="gray",
            anchor="w"
        )
        variants_label.pack(anchor="w")
        
        # Match score
        if "score" in font:
            score_label = ctk.CTkLabel(
                info_frame,
                text=f"Match: {font['score']}%",
                font=ctk.CTkFont(size=11),
                text_color="lightblue",
                anchor="w"
            )
            score_label.pack(anchor="w")
        
        # Right side: Download button
        download_btn = ctk.CTkButton(
            card,
            text="Download",
            width=120,
            command=lambda: self._download_font(source_name, font)
        )
        download_btn.pack(side="right", padx=15, pady=10)
    
    def _download_font(self, source_name: str, font: dict):
        """Download a font."""
        font_name = font["name"]
        font_id = font["source_id"]
        
        # Disable all download buttons
        for widget in self.results_frame.winfo_children():
            for child in widget.winfo_children():
                if isinstance(child, ctk.CTkButton):
                    child.configure(state="disabled")
        
        self._update_status(f"Downloading {font_name}...", "orange")
        
        def download_thread():
            try:
                files = self.manager.download(source_name, font_id)
                self.after(0, lambda: self._download_success(font_name, files))
            except Exception as e:
                self.after(0, lambda: self._download_error(font_name, str(e)))
        
        threading.Thread(target=download_thread, daemon=True).start()
    
    def _download_success(self, font_name: str, files: list):
        """Handle successful download."""
        # Re-enable download buttons
        for widget in self.results_frame.winfo_children():
            for child in widget.winfo_children():
                if isinstance(child, ctk.CTkButton):
                    child.configure(state="normal")
        
        self._update_status(f"✅ Downloaded {font_name} ({len(files)} files)", "green")
        
        messagebox.showinfo(
            "Download Complete",
            f"Successfully downloaded {font_name}\n\n"
            f"Files: {len(files)}\n"
            f"Location: {self.config.output_dir}"
        )
    
    def _download_error(self, font_name: str, error: str):
        """Handle download error."""
        # Re-enable download buttons
        for widget in self.results_frame.winfo_children():
            for child in widget.winfo_children():
                if isinstance(child, ctk.CTkButton):
                    child.configure(state="normal")
        
        self._update_status(f"Failed to download {font_name}", "red")
        messagebox.showerror("Download Error", f"Failed to download {font_name}:\n{error}")
    
    def _open_settings(self):
        """Open settings dialog."""
        settings_window = SettingsDialog(self, self.config)
        settings_window.grab_set()  # Modal dialog


class SettingsDialog(ctk.CTkToplevel):
    """Settings dialog window."""
    
    def __init__(self, parent, config: Config):
        super().__init__(parent)
        
        self.config = config
        self.parent = parent
        
        self.title("Settings")
        self.geometry("400x250")
        
        # Make modal
        self.transient(parent)
        
        self._build_ui()
    
    def _build_ui(self):
        """Build settings UI."""
        # Output directory
        dir_frame = ctk.CTkFrame(self)
        dir_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(
            dir_frame,
            text="Output Directory:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=10, pady=(10, 5))
        
        dir_inner = ctk.CTkFrame(dir_frame, fg_color="transparent")
        dir_inner.pack(fill="x", padx=10, pady=(0, 10))
        
        self.dir_var = ctk.StringVar(value=self.config.output_dir)
        dir_entry = ctk.CTkEntry(
            dir_inner,
            textvariable=self.dir_var,
            state="readonly"
        )
        dir_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        browse_btn = ctk.CTkButton(
            dir_inner,
            text="Browse",
            width=80,
            command=self._browse_directory
        )
        browse_btn.pack(side="right")
        
        # Theme
        theme_frame = ctk.CTkFrame(self)
        theme_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(
            theme_frame,
            text="Theme:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=10, pady=(10, 5))
        
        self.theme_var = ctk.StringVar(value=self.config.get("theme", "dark"))
        theme_menu = ctk.CTkOptionMenu(
            theme_frame,
            variable=self.theme_var,
            values=["dark", "light", "system"]
        )
        theme_menu.pack(fill="x", padx=10, pady=(0, 10))
        
        # Buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=20)
        
        cancel_btn = ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=self.destroy
        )
        cancel_btn.pack(side="right", padx=(5, 0))
        
        save_btn = ctk.CTkButton(
            button_frame,
            text="Save",
            command=self._save_settings
        )
        save_btn.pack(side="right")
    
    def _browse_directory(self):
        """Browse for output directory."""
        directory = filedialog.askdirectory(
            title="Select Output Directory",
            initialdir=self.dir_var.get()
        )
        
        if directory:
            self.dir_var.set(directory)
    
    def _save_settings(self):
        """Save settings and close."""
        # Update config
        self.config.output_dir = self.dir_var.get()
        self.config.set("theme", self.theme_var.get())
        
        # Update parent
        self.parent.manager.output_dir = Path(self.config.output_dir)
        self.parent._update_status(f"Ready | Output: {self.config.output_dir}", "gray")
        
        # Apply theme
        ctk.set_appearance_mode(self.theme_var.get())
        
        messagebox.showinfo("Settings Saved", "Settings have been updated successfully")
        self.destroy()


def main():
    """Application entry point."""
    app = FontGrabber()
    app.mainloop()


if __name__ == "__main__":
    main()
