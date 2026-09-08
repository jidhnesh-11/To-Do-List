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
    },
    "dark2": {
        "header_color": "#29232F",
        "current_date": "#F4EEF5",
        "content_BG": "#17131C",
        "sidebar_BG": "#241E2A",
        "add_task_label_color": "#B9A5BD",
        "toplevel_BG": "#17131C",
        "nav_btn_color": "#382F3D",
        "active_nav_btn": "#624B69",
        "btn_colors": "#F4EEF5",
        "btn_bg": "#4A3A50",
        "tl_color": "#241E2A",
        "tl_font_col": "#F4EEF5",
        "high_priority_color": "#E06A7A",
        "medium_priority_color": "#D6AA4C",
        "low_priority_color": "#72A67D"
        },
    "dark3": {
        "header_color": "#26352B",
        "current_date": "#FFEC81",
        "content_BG": "#40211E",
        "sidebar_BG": "#1D2821",
        "add_task_label_color": "#A4B095",
        "toplevel_BG": "#111713",
        "nav_btn_color": "#3B2A29",
        "active_nav_btn": "#82524F",
        "btn_colors": "#DACB74",
        "btn_bg": "#4A3B30",
        "tl_color": "#1D2821",
        "tl_font_col": "#E7D258",
        "high_priority_color": "#C35C4C",
        "medium_priority_color": "#C49A46",
        "low_priority_color": "#70A078"
    },
    "eg": {
        "header_color": "#40372A",
        "current_date": "#FFE8A3",
        "content_BG": "#181912",
        "sidebar_BG": "#2C2D20",
        "add_task_label_color": "#E3C96A",
        "toplevel_BG": "#181912",
        "nav_btn_color": "#3C432D",
        "active_nav_btn": "#687548",
        "btn_colors": "#FFF1B8",
        "btn_bg": "#594A35",
        "tl_color": "#2C2D20",
        "tl_font_col": "#FFF1B8",
        "high_priority_color": "#C15C4B",
        "medium_priority_color": "#D4A943",
        "low_priority_color": "#76965D"
    },
    "yelo": {
        "header_color": "#526D9B",
        "current_date": "#344765",
        "content_BG": "#F1F5FA",
        "sidebar_BG": "#D0DCEC",
        "add_task_label_color": "#637DA7",
        "toplevel_BG": "#F1F5FA",
        "nav_btn_color": "#B8C7DE",
        "active_nav_btn": "#718CB8",
        "btn_colors": "#344765",
        "btn_bg": "#DDE5F0",
        "tl_color": "#D0DCEC",
        "tl_font_col": "#344765",
        "high_priority_color": "#C75A69",
        "medium_priority_color": "#C39A4B",
        "low_priority_color": "#668B78"
    },

    "blu": {
        "header_color": "#26344E",
        "current_date": "#EEF4FF",
        "content_BG": "#111722",
        "sidebar_BG": "#1C2638",
        "add_task_label_color": "#A6B7D2",
        "toplevel_BG": "#111722",
        "nav_btn_color": "#293852",
        "active_nav_btn": "#4E6590",
        "btn_colors": "#EEF4FF",
        "btn_bg": "#394D70",
        "tl_color": "#1C2638",
        "tl_font_col": "#EEF4FF",
        "high_priority_color": "#DF6878",
        "medium_priority_color": "#D3A94D",
        "low_priority_color": "#70A286"
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
#font_name = "Comic Sans MS"
#font_name= "Century Schoolbook"

#font_name=font= "Edwardian Script ITC"
#font_name ="Footlight MT Light"

######## lol 
font_name= "MS Reference Specialty"


high_circle = "●"
medium_circle = "●"
low_circle = "●"

#fontss