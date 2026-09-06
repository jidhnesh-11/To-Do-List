# themes.py

THEMES = {
    "pastel": {
        "header_color": "#3368A0",
        "current_date": "#021526",
        "content_BG": "#FDF4D2",
        "sidebar_BG": "#66A3BF",
        "add_task_label_color": "#6096B4",
        "toplevel_BG": "#FDF4D2",
        "nav_btn_color": "#4BB8FA",
        "active_nav_btn": "#3572EF",
        "btn_colors": "#021526",
        "btn_bg": "#AEE2FF",
        "tl_color": "#66A3BF",
        "tl_font_col": "#021526",
        "high_priority_color": "#EF4444",
        "medium_priority_color": "#F59E0B",
        "low_priority_color": "#10B981",
    },
    "dark": {
        "header_color": "#1E293B",
        "current_date": "#F8FAFC",
        "content_BG": "#0F172A",
        "sidebar_BG": "#1E293B",
        "add_task_label_color": "#94A3B8",
        "toplevel_BG": "#0F172A",
        "nav_btn_color": "#334155",
        "active_nav_btn": "#475569",
        "btn_colors": "#F8FAFC",
        "btn_bg": "#475569",
        "tl_color": "#1E293B",
        "tl_font_col": "#F8FAFC",
        "high_priority_color": "#F87171",
        "medium_priority_color": "#FBBF24",
        "low_priority_color": "#34D399",
    },
    "vintage": {
        "header_color": "#6B4F4F",
        "current_date": "#3E2C2C",
        "content_BG": "#F5E6D3",
        "sidebar_BG": "#D4B499",
        "add_task_label_color": "#8B5E3C",
        "toplevel_BG": "#F5E6D3",
        "nav_btn_color": "#C4A484",
        "active_nav_btn": "#A0522D",
        "btn_colors": "#3E2C2C",
        "btn_bg": "#E6CCB2",
        "tl_color": "#D4B499",
        "tl_font_col": "#3E2C2C",
        "high_priority_color": "#C0392B",
        "medium_priority_color": "#D4A017",
        "low_priority_color": "#6B8E23",
    }
}

# Default theme
current_theme = "pastel"

# f(x) to set colors based on current themeeeee!
def apply_theme(theme_name):
    global current_theme
    if theme_name not in THEMES:
        return
    current_theme = theme_name
    colors = THEMES[theme_name]
    for key, value in colors.items():
        globals()[key] = value

#default themeeeee
apply_theme("pastel")

#font and symbols remain constant across themes
font_name = "Comic Sans MS"
high_circle = "●"
medium_circle = "●"
low_circle = "●"