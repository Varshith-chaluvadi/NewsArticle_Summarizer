// ============================================================
// Configuration
// ============================================================
// Replace this URL with your HuggingFace Spaces URL after deployment.
// Example: "https://tharun-7733-news-summarizer.hf.space"
const API_BASE_URL = "https://tharuntej7373-news-article-summarizer.hf.space";

// ============================================================
// DOM Elements
// ============================================================
const form = document.getElementById("summarize-form");
const urlInput = document.getElementById("article-url-input");
const submitBtn = document.getElementById("summarize-btn");
const btnText = submitBtn.querySelector(".btn-text");
const btnIcon = submitBtn.querySelector(".btn-icon");

const errorDisplay = document.getElementById("error-display");
const errorText = document.getElementById("error-text");
const loadingDisplay = document.getElementById("loading-display");
const summarySection = document.getElementById("summary-section");
const summaryText = document.getElementById("summary-text");
const imagesSection = document.getElementById("images-section");
const imagesGrid = document.getElementById("images-grid");

// ============================================================
// Helpers
// ============================================================
function showElement(el) {
    el.classList.remove("hidden");
}

function hideElement(el) {
    el.classList.add("hidden");
}

function resetResults() {
    hideElement(errorDisplay);
    hideElement(summarySection);
    hideElement(imagesSection);
    imagesGrid.innerHTML = "";
}

function showError(message) {
    errorText.textContent = message;
    showElement(errorDisplay);
}

function setLoading(isLoading) {
    if (isLoading) {
        submitBtn.disabled = true;
        btnText.textContent = "Summarizing…";
        showElement(loadingDisplay);
    } else {
        submitBtn.disabled = false;
        btnText.textContent = "Summarize";
        hideElement(loadingDisplay);
    }
}

// ============================================================
// Main Form Handler
// ============================================================
form.addEventListener("submit", async (e) => {
    e.preventDefault();
    resetResults();

    const url = urlInput.value.trim();
    if (!url) {
        showError("Please enter a valid URL.");
        return;
    }

    setLoading(true);

    try {
        const response = await fetch(`${API_BASE_URL}/summarize`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url }),
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.error || "Something went wrong. Please try again.");
            return;
        }

        // Show summary
        if (data.summary) {
            summaryText.textContent = data.summary;
            showElement(summarySection);
        }

        // Show images
        if (data.images && data.images.length > 0) {
            data.images.forEach((src) => {
                const card = document.createElement("div");
                card.className = "image-card";
                const img = document.createElement("img");
                img.src = src;
                img.alt = "Article image";
                img.loading = "lazy";
                img.onerror = () => card.remove();
                card.appendChild(img);
                imagesGrid.appendChild(card);
            });
            showElement(imagesSection);
        }
    } catch (err) {
        showError("Could not connect to the API. Is the backend running?");
        console.error("Fetch error:", err);
    } finally {
        setLoading(false);
    }
});
