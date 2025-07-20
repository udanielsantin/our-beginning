// Timer original
document.addEventListener('DOMContentLoaded', () => {
  const targetDate = new Date('2025-05-20T22:12:00');

  const labels = ['Anos', 'Meses', 'Dias', 'Horas', 'Min', 'Seg'];
  const timerDiv = document.getElementById('timer');

  labels.forEach(label => {
    const box = document.createElement('div');
    box.className = 'timer-box';
    box.innerHTML = `<span id="${label.toLowerCase()}">00</span><small>${label}</small>`;
    timerDiv.appendChild(box);
  });

  function pad(num) {
    return String(num).padStart(2, '0');
  }

  function calcElapsed(from, to) {
    let start = new Date(from);
    let end = new Date(to);

    let years = end.getFullYear() - start.getFullYear();
    let months = end.getMonth() - start.getMonth();
    let days = end.getDate() - start.getDate();
    let hours = end.getHours() - start.getHours();
    let minutes = end.getMinutes() - start.getMinutes();
    let seconds = end.getSeconds() - start.getSeconds();

    if (seconds < 0) { seconds += 60; minutes--; }
    if (minutes < 0) { minutes += 60; hours--; }
    if (hours < 0)   { hours += 24; days--; }

    if (days < 0) {
      const prevMonth = new Date(end.getFullYear(), end.getMonth(), 0).getDate();
      days += prevMonth;
      months--;
    }

    if (months < 0) {
      months += 12;
      years--;
    }

    return { years, months, days, hours, minutes, seconds };
  }

  function updateElapsed() {
    const now = new Date();
    const elapsed = calcElapsed(targetDate, now);

    document.getElementById('anos').textContent   = pad(elapsed.years);
    document.getElementById('meses').textContent  = pad(elapsed.months);
    document.getElementById('dias').textContent   = pad(elapsed.days);
    document.getElementById('horas').textContent  = pad(elapsed.hours);
    document.getElementById('min').textContent    = pad(elapsed.minutes);
    document.getElementById('seg').textContent    = pad(elapsed.seconds);
  }

  updateElapsed();
  setInterval(updateElapsed, 1000);
});

// 💖 Corações animados caindo
function criarCoracao() {
  const heart = document.createElement('div');
  heart.classList.add('heart');
  heart.style.left = Math.random() * window.innerWidth + 'px';
  heart.style.animationDuration = (Math.random() * 4 + 6) + 's'; // velocidade variável

  document.body.appendChild(heart);

  // Remove após a animação
  setTimeout(() => {
    heart.remove();
  }, 11000);
}

// Cria corações em intervalos aleatórios
setInterval(criarCoracao, 700);
