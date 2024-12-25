from flask import Flask, render_template, request
from scheduler import FCFS, SJF, RoundRobin

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        algorithm = request.form["algorithm"]
        processes = []
        for i in range(int(request.form["num_processes"])):
            arrival_time = int(request.form[f"arrival_time_{i}"])
            burst_time = int(request.form[f"burst_time_{i}"])
            processes.append((arrival_time, burst_time))
        
        if algorithm == "FCFS":
            result = FCFS(processes)
        elif algorithm == "SJF":
            result = SJF(processes)
        elif algorithm == "RoundRobin":
            time_quantum = int(request.form["time_quantum"])
            result = RoundRobin(processes, time_quantum)
        
        return render_template("index.html", result=result, processes=processes, algorithm=algorithm)
    
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
