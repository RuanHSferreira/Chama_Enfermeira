import tkinter

window = tkinter.Tk()
window.geometry("200x200")

limit = 80
# score = 0

def update(score):
    # global score
    m, s = divmod(score, 60)
    min_for = f"{m:02d}:{s:02d}"
    score += 1
    ScoreL.configure(text=min_for)
    if score < limit:
        # schedule next update 1 second later
        window.after(1000, update, score)

ScoreL = tkinter.Label(window, text="00:00", font=20)
ScoreL.pack()

window.after(1000, update, 0) # start the update 1 second later
window.mainloop()