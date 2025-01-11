import tkinter as tk
from tkinter import messagebox
import csv
import json
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EVM:
    def __init__(self):
        self.candidates = {}
        self.voted_phone_numbers = set()

    def add_candidates(self, candidate_names):
        self.candidates = {candidate: 0 for candidate in candidate_names}

    def add_voter(self, phone_number):
        if phone_number not in self.voted_phone_numbers:
            self.voted_phone_numbers.add(phone_number)
            return True
        else:
            return False

    def cast_vote(self, phone_number, vote_choice):
        if phone_number in self.voted_phone_numbers:
            return False
        else:
            if vote_choice in self.candidates:
                self.candidates[vote_choice] += 1
                self.voted_phone_numbers.add(phone_number)
                return True
            else:
                return False

    def show_candidates(self):
        return list(self.candidates.keys())

    def show_results(self):
        return self.candidates

    def export_results_csv(self, filename="voting_results.csv"):
        results = self.show_results()
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Candidate", "Votes"])
            for candidate, votes in results.items():
                writer.writerow([candidate, votes])

    def export_results_json(self, filename="voting_results.json"):
        results = self.show_results()
        with open(filename, 'w') as file:
            json.dump(results, file, indent=4)

class EVMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EVM Voting System")
        self.root.geometry("700x700")
        self.root.config(bg="#F0F0F0")
        self.evm = EVM()
        self.admin_password = "admin123"
        self.is_dark_mode = False
        self.create_main_screen()
        self.add_creator_name()

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        bg_color = "#2E2E2E" if self.is_dark_mode else "#F0F0F0"
        fg_color = "white" if self.is_dark_mode else "black"
        self.root.config(bg=bg_color)
        for widget in self.root.winfo_children():
            widget.config(bg=bg_color, fg=fg_color)

    def create_main_screen(self):
        self.main_frame = tk.Frame(self.root, bg="#F0F0F0", bd=2, highlightbackground="black", highlightthickness=2)
        self.main_frame.pack(pady=20)

        tk.Button(self.main_frame, text="Admin Panel", width=20, bg="#4CAF50", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.show_admin_panel).pack(pady=10)
        tk.Button(self.main_frame, text="Voter Panel", width=20, bg="#2196F3", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.show_voter_panel).pack(pady=10)
        tk.Button(self.main_frame, text="Results Panel", width=20, bg="#FF9800", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.show_results_panel).pack(pady=10)
        tk.Button(self.main_frame, text="Instructions", width=20, bg="#FFC107", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.show_instructions).pack(pady=10)
        tk.Button(self.main_frame, text="Toggle Theme", width=20, bg="#9C27B0", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.toggle_theme).pack(pady=10)
        tk.Button(self.main_frame, text="Exit", width=20, bg="#f44336", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.root.quit).pack(pady=10)

    def add_creator_name(self):
        creator_label = tk.Label(self.root, text="Created by Hrishikesh Shahane", font=("Arial", 10),
                                 bg="#F0F0F0", anchor="w")
        creator_label.place(relx=0.02, rely=0.96, anchor="w")

    def show_admin_panel(self):
        self.main_frame.pack_forget()
        self.admin_frame = tk.Frame(self.root, bg="#F0F0F0", bd=2, highlightbackground="black", highlightthickness=2)
        self.admin_frame.pack(pady=20)

        tk.Label(self.admin_frame, text="Enter Candidate Names (comma-separated)", font=("Arial", 14), bg="#F0F0F0").pack(pady=10)
        self.candidate_names_entry = tk.Entry(self.admin_frame, width=30, font=("Arial", 12), bd=2, highlightbackground="black")
        self.candidate_names_entry.pack(pady=10)

        tk.Button(self.admin_frame, text="Add Candidates", bg="#4CAF50", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.add_candidates).pack(pady=10)
        tk.Button(self.admin_frame, text="Reset System", bg="#FF5722", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.reset_system).pack(pady=10)
        tk.Button(self.admin_frame, text="Back", bg="#FF5722", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.back_to_main).pack(pady=10)

    def add_candidates(self):
        candidate_names_str = self.candidate_names_entry.get()
        if candidate_names_str:
            candidate_names = [name.strip() for name in candidate_names_str.split(",")]
            if len(candidate_names) > 0:
                self.evm.add_candidates(candidate_names)
                messagebox.showinfo("Success", "Candidates added successfully!")
                self.candidate_names_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter valid candidate names.")
        else:
            messagebox.showerror("Error", "Please enter candidate names.")

    def show_voter_panel(self):
        self.main_frame.pack_forget()
        self.voter_frame = tk.Frame(self.root, bg="#F0F0F0", bd=2, highlightbackground="black", highlightthickness=2)
        self.voter_frame.pack(pady=20)

        tk.Label(self.voter_frame, text="Enter your Phone Number", font=("Arial", 14), bg="#F0F0F0").pack(pady=10)
        self.phone_entry = tk.Entry(self.voter_frame, width=30, font=("Arial", 12), bd=2, highlightbackground="black")
        self.phone_entry.pack(pady=10)

        self.candidates_listbox = tk.Listbox(self.voter_frame, width=30, height=10, font=("Arial", 12), bd=2, highlightbackground="black")
        self.update_candidates_listbox()
        self.candidates_listbox.pack(pady=10)

        tk.Button(self.voter_frame, text="Cast Vote", bg="#4CAF50", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.cast_vote).pack(pady=10)
        tk.Button(self.voter_frame, text="Back", bg="#FF5722", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.back_to_main).pack(pady=10)

    def update_candidates_listbox(self):
        self.candidates_listbox.delete(0, tk.END)
        candidates = self.evm.show_candidates()
        for candidate in candidates:
            self.candidates_listbox.insert(tk.END, candidate)

    def cast_vote(self):
        phone_number = self.phone_entry.get()
        selected_candidate = self.candidates_listbox.get(tk.ACTIVE)
        if phone_number and selected_candidate:
            if self.evm.cast_vote(phone_number, selected_candidate):
                messagebox.showinfo("Success", f"Vote cast successfully for {selected_candidate}")
            else:
                messagebox.showerror("Error", "This phone number has already voted.")
        else:
            messagebox.showerror("Error", "Please enter a valid phone number and select a candidate.")

    def show_results_panel(self):
        self.main_frame.pack_forget()
        self.results_frame = tk.Frame(self.root, bg="#F0F0F0", bd=2, highlightbackground="black", highlightthickness=2)
        self.results_frame.pack(pady=20)

        tk.Label(self.results_frame, text="Enter Admin Password", font=("Arial", 14), bg="#F0F0F0").pack(pady=10)
        self.password_entry = tk.Entry(self.results_frame, width=30, show="*", font=("Arial", 12), bd=2, highlightbackground="black")
        self.password_entry.pack(pady=10)

        tk.Button(self.results_frame, text="Show Results", bg="#4CAF50", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.show_results).pack(pady=10)
        tk.Button(self.results_frame, text="Export to CSV", bg="#2196F3", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.export_results_csv).pack(pady=10)
        tk.Button(self.results_frame, text="Export to JSON", bg="#FFC107", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.export_results_json).pack(pady=10)
        tk.Button(self.results_frame, text="Back", bg="#FF5722", fg="white", font=("Arial", 14),
                  bd=2, highlightbackground="black", command=self.back_to_main).pack(pady=10)

    def show_results(self):
        password = self.password_entry.get()
        if password == self.admin_password:
            self.display_results_chart()
        else:
            messagebox.showerror("Error", "Incorrect password. Access denied.")

    def display_results_chart(self):
        results = self.evm.show_results()
        candidates = list(results.keys())
        votes = list(results.values())

        plt.figure(figsize=(8, 5))
        plt.pie(votes, labels=candidates, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
        plt.title("Live Voting Results")
        plt.show()

    def export_results_csv(self):
        self.evm.export_results_csv()
        messagebox.showinfo("Success", "Results exported to CSV successfully!")

    def export_results_json(self):
        self.evm.export_results_json()
        messagebox.showinfo("Success", "Results exported to JSON successfully!")

    def reset_system(self):
        if messagebox.askyesno("Confirm Reset", "Are you sure you want to reset the voting system? This will erase all data."):
            self.evm = EVM()
            messagebox.showinfo("Success", "System reset successfully!")

    def show_instructions(self):
        instructions = """Instructions:
1. Admin Panel: Add candidates and reset the system.
2. Voter Panel: Enter your phone number and vote for your preferred candidate.
3. Results Panel: Admin can view live results by entering the password.
4. Toggle Theme: Switch between light and dark modes for better visibility.
        """
        messagebox.showinfo("Instructions", instructions)

    def back_to_main(self):
        for frame in self.root.winfo_children():
            frame.pack_forget()
        self.create_main_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = EVMApp(root)
    root.mainloop()
