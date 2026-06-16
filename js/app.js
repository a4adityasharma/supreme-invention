const form = document.getElementById('sentiment-form');
const input = document.getElementById('video-input');
const resultSection = document.getElementById('result');
const sentimentOutput = document.getElementById('sentiment-output');
const scoreOutput = document.getElementById('score-output');

form.addEventListener('submit', event => {
  event.preventDefault();
  const text = input.value.trim();

  if (!text) return;

  sentimentOutput.textContent = 'Analyzing...';
  scoreOutput.textContent = '';
  resultSection.classList.remove('hidden');

  fetch('/api/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text })
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        sentimentOutput.textContent = `Error: ${data.error}`;
        scoreOutput.textContent = '';
        return;
      }

      sentimentOutput.textContent = `Sentiment: ${data.sentiment}`;
      scoreOutput.textContent = `Sentiment score: ${data.score.toFixed(3)} (higher is more positive)`;
    })
    .catch(error => {
      sentimentOutput.textContent = 'Could not analyze sentiment.';
      scoreOutput.textContent = error.message;
    });
});
