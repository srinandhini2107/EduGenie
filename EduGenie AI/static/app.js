async function sendRequest(url, data) {

    const response = await fetch(url, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    });

    return await response.json();
}


/* ---------------- QUESTION ---------------- */

async function askQuestion() {

    const question =
        document.getElementById("question").value;

    const box =
        document.getElementById("answer");

    box.innerHTML = "Thinking...";

    try {

        const data = await sendRequest(
            "/api/qna",
            {
                question: question
            }
        );

        box.innerHTML =
            "<b>Answer:</b><br>" +
            formatText(data.result);

    } catch (error) {

        box.innerHTML =
            "Error connecting to AI.";

    }
}


/* ---------------- EXPLANATION ---------------- */

async function explainTopic() {

    const topic =
        document.getElementById("topic").value;

    const box =
        document.getElementById("explanation");

    box.innerHTML = "Generating explanation...";

    try {

        const data = await sendRequest(
            "/api/explain",
            {
                topic: topic
            }
        );

        box.innerHTML =
            "<b>Explanation:</b><br>" +
            formatText(data.result);

    } catch (error) {

        box.innerHTML =
            "Error connecting to AI.";

    }
}


/* ---------------- SUMMARY ---------------- */

async function summarize() {

    const text =
        document.getElementById("paragraph").value;

    const box =
        document.getElementById("summary");

    box.innerHTML = "Summarizing...";

    try {

        const data = await sendRequest(
            "/api/summary",
            {
                text: text
            }
        );

        box.innerHTML =
            "<b>Summary:</b><br>" +
            formatText(data.result);

    } catch (error) {

        box.innerHTML =
            "Error connecting to AI.";

    }
}


/* ---------------- QUIZ ---------------- */

async function generateQuiz() {

    const topic =
        document.getElementById("quizTopic").value;

    const box =
        document.getElementById("quiz");

    box.innerHTML = "Generating quiz...";

    try {

        const data = await sendRequest(
            "/api/quiz",
            {
                topic: topic
            }
        );

        if (data.error) {

            box.innerHTML =
                "Error: " + data.error;

            return;
        }

        displayQuiz(data.quiz);

    } catch (error) {

        box.innerHTML =
            "Error generating quiz.";

    }
}


/* ---------------- DISPLAY QUIZ ---------------- */

function displayQuiz(questions) {

    const box =
        document.getElementById("quiz");

    box.innerHTML = "";

    questions.forEach((item, index) => {

        const questionDiv =
            document.createElement("div");

        questionDiv.className =
            "quiz-question";

        let html = "";

        html +=
            "<h3>Question " +
            (index + 1) +
            "</h3>";

        html +=
            "<p><b>" +
            item.question +
            "</b></p>";

        item.options.forEach((option) => {

            html += `
                <button
                    class="option-button"
                    onclick="checkAnswer(
                        this,
                        '${escapeText(option)}',
                        '${escapeText(item.answer)}',
                        '${escapeText(item.explanation)}'
                    )">
                    ${option}
                </button>
            `;

        });

        html +=
            '<p class="quiz-result"></p>';

        questionDiv.innerHTML = html;

        box.appendChild(questionDiv);

    });
}


/* ---------------- CHECK ANSWER ---------------- */

function checkAnswer(
    button,
    selected,
    correct,
    explanation
) {

    const parent =
        button.parentElement;

    const result =
        parent.querySelector(".quiz-result");

    const buttons =
        parent.querySelectorAll(
            ".option-button"
        );

    buttons.forEach(btn => {

        btn.disabled = true;

    });


    if (selected === correct) {

        result.innerHTML =
            "✅ Correct!<br>" +
            explanation;

    } else {

        result.innerHTML =
            "❌ Wrong answer.<br>" +
            "Correct answer: " +
            correct +
            "<br>" +
            explanation;

    }
}


/* ---------------- RECOMMENDATION ---------------- */

async function recommendTopic() {

    const topic =
        document.getElementById("recommend").value;

    const box =
        document.getElementById("recommendation");

    box.innerHTML =
        "Generating recommendations...";

    try {

        const data = await sendRequest(
            "/api/learning-path",
            {
                topic: topic
            }
        );

        box.innerHTML =
            "<b>Learning Recommendations:</b><br>" +
            formatText(data.result);

    } catch (error) {

        box.innerHTML =
            "Error generating recommendations.";

    }
}


/* ---------------- TEXT FORMAT ---------------- */

function formatText(text) {

    if (!text) {
        return "";
    }

    return text
        .replace(/\*\*(.*?)\*\*/g, "<b>$1</b>")
        .replace(/\n/g, "<br>");
}


function escapeText(text) {

    return text
        .replace(/'/g, "\\'")
        .replace(/"/g, "&quot;");
}