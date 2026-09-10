import tkinter as tk
import themes as th
import auth_db as audb
import ui


def showAuthWin(login_window, window):
    current_mode = "signup"   # start in signup mode

    def update_view_signup():
        nonlocal current_mode
        current_mode = "signup"
        #confirm_btn.config(text="Sign Up!")
        signup_btn.config(bg=th.active_nav_btn, fg="white")
        login_btn.config(bg=th.content_BG, fg=th.current_date)

    def update_view_login():
        nonlocal current_mode
        current_mode = "login"
        #confirm_btn.config(text="Log In!")
        login_btn.config(bg=th.active_nav_btn, fg="white")
        signup_btn.config(bg=th.content_BG, fg=th.current_date)

    def confirm_action():
        username = username_entry.get().strip()
        password = pass_entry.get().strip()

        if not username or not password:
            msg_box.config(text="Please fill all the fields", fg="red")
            return

        if current_mode == "signup":
            success, message = audb.signup(username, password)
            if success:
                msg_box.config(text=message, fg="green")
                username_entry.delete(0, tk.END)
                pass_entry.delete(0, tk.END)
                update_view_login()
            else:
                msg_box.config(text=message, fg="red")
        else:
            if audb.login(username, password):
                msg_box.config(text="Login Successful!", fg="green")
                #theme_name = audb.get_theme(username)  # optional
                #th.apply_theme(theme_name)
                login_window.destroy()
                window.deiconify()
                ui.showWidget(window, username)
            else:
                msg_box.config(text="Invalid credentials", fg="red")

    # Main container
    main_frame = tk.Frame(login_window, bg=th.content_BG, padx=30, pady=20)
    main_frame.pack(expand=True, fill="both")

    # Make the main_frame expand nicely
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(2, weight=1)

    # brand name 
    top_frame = tk.Frame(main_frame, bg=th.content_BG)
    top_frame.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 10))

    brand_name = tk.Label(top_frame, text="DoDoingDone",
                          font=(th.font_name, 20, "bold"),
                          bg=th.content_BG, fg=th.current_date)
    brand_name.pack(side="left")

    # Right-side toggle frame 
    toggle_frame = tk.Frame(top_frame, bg=th.content_BG)
    toggle_frame.pack(side="right")

    signup_btn = tk.Button(toggle_frame, text="Sign Up",
                           font=(th.font_name, 10, "bold"),
                           bg=th.active_nav_btn, fg="white",
                           relief="flat", padx=8, pady=2,
                           activebackground=th.active_nav_btn,
                           command=update_view_signup)
    signup_btn.pack(side="left")

    tk.Label(toggle_frame, text=" / ",
             font=(th.font_name, 10, "bold"),
             bg=th.content_BG, fg=th.current_date).pack(side="left")

    login_btn = tk.Button(toggle_frame, text="Log In",
                          font=(th.font_name, 10, "bold"),
                          bg=th.content_BG, fg=th.current_date,
                          relief="flat", padx=8, pady=2,
                          activebackground=th.active_nav_btn,
                          command=update_view_login)
    login_btn.pack(side="left")

    #sep line
    sep1 = tk.Frame(main_frame, bg="#60AFE8", height=3)
    sep1.grid(row=1, column=0, columnspan=3, sticky="ew", pady=10)

    # greet
    greeting = tk.Label(main_frame, text="Hello, User!",
                        font=(th.font_name, 14, "bold"),
                        bg=th.content_BG, fg=th.current_date)
    greeting.grid(row=2, column=0, columnspan=3, pady=(5, 15))

    # entry of usrname and passs
    username_label = tk.Label(main_frame, text="Username:",
                              font=(th.font_name, 17, "bold"),
                              bg=th.content_BG, fg=th.current_date)
    username_label.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=8)

    username_entry = tk.Entry(main_frame, width=25,
                              font=(th.font_name, 11),
                              bg="white", relief="solid", bd=1)
    username_entry.grid(row=3, column=1, padx=(0, 10), pady=8, ipady=4)

    pass_label = tk.Label(main_frame, text="Password:",
                          font=(th.font_name, 17, "bold"),
                          bg=th.content_BG, fg=th.current_date)
    pass_label.grid(row=4, column=0, sticky="e", padx=(0, 10), pady=8)

    pass_entry = tk.Entry(main_frame, width=25, show="*",
                          font=(th.font_name, 11),
                          bg="white", relief="solid", bd=1)
    pass_entry.grid(row=4, column=1, padx=(0, 10), pady=8, ipady=4)

    #confirm btn
    confirm_btn = tk.Button(main_frame, text="Confirm! ->",
                            font=(th.font_name, 12, "bold"),
                            bg=th.nav_btn_color, fg=th.btn_colors,
                            activebackground=th.active_nav_btn,
                            relief="flat", padx=20, pady=5,
                            command=confirm_action)
    confirm_btn.grid(row=5, column=0, columnspan=3, pady=(15, 5))

    # last msg box 
    msg_box = tk.Label(main_frame, text="",
                       font=(th.font_name, 11, "bold"),
                       bg=th.content_BG, fg="red")
    msg_box.grid(row=6, column=0, columnspan=3, pady=(5, 0))