

// ====================
// PDF Upload
// ====================
async function uploadPDF() {
    const file = document.getElementById("pdf").files[0];
    const status = document.getElementById("uploadStatus");

    if (!file) {
        status.className = "alert alert-danger";
        status.innerText = "Select a PDF first";
        status.classList.remove("d-none");
        return;
    }

    const fd = new FormData();
    fd.append("file", file);  // IMPORTANT: must match FastAPI param name

    status.className = "alert alert-info";
    status.innerText = "Uploading PDF...";
    status.classList.remove("d-none");

    const res = await fetch("/api/upload", {
        method: "POST",
        body: fd
    });

    const data = await res.json();

    if (data.success) {
        status.className = "alert alert-success";
        status.innerText = data.message;
    } else {
        status.className = "alert alert-danger";
        status.innerText = data.message;
    }
}



// ====================
// Ask Question
// ====================
async function askQuestion() {
    if (!uploaded) {
        alert("Upload PDF first");
        return;
    }

    const q = document.getElementById("question").value;
    const box = document.getElementById("answerBox");
    const askBtn = document.getElementById("askBtn");

    if (!q.trim()) {
        alert("Enter a question");
        return;
    }

    const fd = new FormData();
    fd.append("question", q);

    // Show processing message
    box.className = "alert alert-warning mt-3";
    box.innerText = "Processing question...";
    box.classList.remove("d-none");

    askBtn.disabled = true;

    try {
        const res = await fetch("/api/ask", { method: "POST", body: fd });
        const data = await res.json();

        box.className = "alert alert-info mt-3";
        box.innerHTML = "<strong>Answer:</strong><br>" + (data.answer || "No answer returned.");
    } catch (error) {
        box.className = "alert alert-danger mt-3";
        box.innerText = "Error processing question.";
    }

    askBtn.disabled = false;
}
