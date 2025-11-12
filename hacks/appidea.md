---
layout: base
title: Snake Game
permalink: /app/
---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EaseCompanion - Elder Care App</title>

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

<style>
  body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    background-color: #f0f4f8;
    color: #222;
  }

  header {
    background-color: #2a6ef7;
    color: white;
    text-align: center;
    padding: 1rem;
    font-size: 1.5rem;
    font-weight: 600;
  }

  nav {
    position: fixed;
    bottom: 0;
    width: 100%;
    display: flex;
    background-color: #fff;
    border-top: 1px solid #ccc;
  }

  nav button {
    flex: 1;
    padding: 0.8rem 0;
    border: none;
    background: none;
    font-size: 0.9rem;
    cursor: pointer;
    color: #555;
    transition: 0.3s;
  }

  nav button.active {
    color: #2a6ef7;
    font-weight: 600;
  }

  main {
    padding: 1rem;
    padding-bottom: 5rem;
  }

  section {
    display: none;
  }

  section.active {
    display: block;
  }

  .card {
    background-color: white;
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }

  input, textarea {
    width: 100%;
    padding: 0.6rem;
    margin-bottom: 0.6rem;
    border-radius: 6px;
    border: 1px solid #ccc;
    font-size: 1rem;
  }

  button.add-btn {
    background-color: #2a6ef7;
    color: white;
    border: none;
    padding: 0.6rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    width: 100%;
    font-size: 1rem;
  }

  h2 {
    margin-top: 0;
  }

  .entry {
    padding: 0.5rem 0;
    border-bottom: 1px solid #eee;
  }

  .entry:last-child {
    border-bottom: none;
  }

  label {
    font-weight: 500;
    margin-top: 0.5rem;
    display: block;
  }
</style>
</head>

<body>
<header>EaseCompanion</header>

<main>
  <!-- Home Section -->
  <section id="home" class="active card">
    <h2>Welcome to EaseCompanion</h2>
    <p>Track pain, medications, exercises, and care notes for seniors. Designed for elderly recovery and family/caregiver support.</p>
  </section>

  <!-- Pain Log Section -->
  <section id="painLog" class="card">
    <h2>Pain Log</h2>
    <textarea id="painText" placeholder="Describe your pain..."></textarea>
    <input type="text" id="painTags" placeholder="Optional tags (knee, hip, etc.)">
    <button class="add-btn" onclick="addPain()">Add Entry</button>
    <div id="painEntries"></div>
  </section>

  <!-- Medication Section -->
  <section id="medications" class="card">
    <h2>Medications</h2>
    <input type="text" id="medName" placeholder="Medication Name">
    <input type="text" id="medDosage" placeholder="Dosage">
    <input type="time" id="medTime">
    <button class="add-btn" onclick="addMed()">Add Medication</button>
    <div id="medList"></div>
  </section>

  <!-- Exercise Section -->
  <section id="exercises" class="card">
    <h2>Exercises</h2>
    <input type="text" id="exName" placeholder="Exercise Name">
    <input type="text" id="exDuration" placeholder="Duration/Time">
    <button class="add-btn" onclick="addExercise()">Add Exercise</button>
    <div id="exList"></div>
  </section>

  <!-- Care Circle Section -->
  <section id="careCircle" class="card">
    <h2>Care Circle</h2>
    <textarea id="noteText" placeholder="Add a note for your loved one"></textarea>
    <button class="add-btn" onclick="addNote()">Add Note</button>
    <div id="noteList"></div>
  </section>

  <!-- Feedback Section -->
  <section id="feedback" class="card">
    <h2>Feedback</h2>
    <input type="text" id="feedbackName" placeholder="Your Name (optional)">
    <textarea id="feedbackText" placeholder="Your feedback"></textarea>
    <button class="add-btn" onclick="submitFeedback()">Submit Feedback</button>
  </section>
</main>

<!-- Navigation -->
<nav>
  <button class="active" onclick="showTab('home', this)">Home</button>
  <button onclick="showTab('painLog', this)">Pain Log</button>
  <button onclick="showTab('medications', this)">Medications</button>
  <button onclick="showTab('exercises', this)">Exercises</button>
  <button onclick="showTab('careCircle', this)">Care Circle</button>
  <button onclick="showTab('feedback', this)">Feedback</button>
</nav>

<script>
  // ------------------ Tabs ------------------
  function showTab(id, btn) {
    document.querySelectorAll('section').forEach(sec => sec.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }

  // ------------------ Pain Log ------------------
  function loadPain() {
    const data = JSON.parse(localStorage.getItem('painEntries') || '[]');
    const container = document.getElementById('painEntries');
    container.innerHTML = '';
    data.forEach(entry => {
      const div = document.createElement('div');
      div.classList.add('entry');
      div.innerHTML = `<strong>${entry.tags || 'General'}</strong>: ${entry.text} <br><small>${entry.date}</small>`;
      container.appendChild(div);
    });
  }

  function addPain() {
    const text = document.getElementById('painText').value;
    const tags = document.getElementById('painTags').value;
    if (!text) return alert('Enter a description.');
    const data = JSON.parse(localStorage.getItem('painEntries') || '[]');
    data.push({ text, tags, date: new Date().toLocaleString() });
    localStorage.setItem('painEntries', JSON.stringify(data));
    document.getElementById('painText').value = '';
    document.getElementById('painTags').value = '';
    loadPain();
  }
  loadPain();

  // ------------------ Medications ------------------
  function loadMeds() {
    const data = JSON.parse(localStorage.getItem('medications') || '[]');
    const container = document.getElementById('medList');
    container.innerHTML = '';
    data.forEach(med => {
      const div = document.createElement('div');
      div.classList.add('entry');
      div.textContent = `${med.name} - ${med.dosage} at ${med.time}`;
      container.appendChild(div);
    });
  }

  function addMed() {
    const name = document.getElementById('medName').value;
    const dosage = document.getElementById('medDosage').value;
    const time = document.getElementById('medTime').value;
    if (!name || !dosage || !time) return alert('Fill all fields.');
    const data = JSON.parse(localStorage.getItem('medications') || '[]');
    data.push({ name, dosage, time });
    localStorage.setItem('medications', JSON.stringify(data));
    document.getElementById('medName').value = '';
    document.getElementById('medDosage').value = '';
    document.getElementById('medTime').value = '';
    loadMeds();
  }
  loadMeds();

  // ------------------ Exercises ------------------
  function loadExercises() {
    const data = JSON.parse(localStorage.getItem('exercises') || '[]');
    const container = document.getElementById('exList');
    container.innerHTML = '';
    data.forEach(ex => {
      const div = document.createElement('div');
      div.classList.add('entry');
      div.textContent = `${ex.name} - ${ex.duration}`;
      container.appendChild(div);
    });
  }

  function addExercise() {
    const name = document.getElementById('exName').value;
    const duration = document.getElementById('exDuration').value;
    if (!name || !duration) return alert('Fill all fields.');
    const data = JSON.parse(localStorage.getItem('exercises') || '[]');
    data.push({ name, duration });
    localStorage.setItem('exercises', JSON.stringify(data));
    document.getElementById('exName').value = '';
    document.getElementById('exDuration').value = '';
    loadExercises();
  }
  loadExercises();

  // ------------------ Care Circle ------------------
  function loadNotes() {
    const data = JSON.parse(localStorage.getItem('careNotes') || '[]');
    const container = document.getElementById('noteList');
    container.innerHTML = '';
    data.forEach(note => {
      const div = document.createElement('div');
      div.classList.add('entry');
      div.innerHTML = `${note.text} <br><small>${note.date}</small>`;
      container.appendChild(div);
    });
  }

  function addNote() {
    const text = document.getElementById('noteText').value;
    if (!text) return alert('Enter a note.');
    const data = JSON.parse(localStorage.getItem('careNotes') || '[]');
    data.push({ text, date: new Date().toLocaleString() });
    localStorage.setItem('careNotes', JSON.stringify(data));
    document.getElementById('noteText').value = '';
    loadNotes();
  }
  loadNotes();

  // ------------------ Feedback ------------------
  function submitFeedback() {
    const name = document.getElementById('feedbackName').value;
    const text = document.getElementById('feedbackText').value;
    if (!text) return alert('Enter feedback.');
    // For prototype, just log to console (or later connect to Google Forms)
    console.log('Feedback:', { name, text });
    alert('Thank you for your feedback!');
    document.getElementById('feedbackName').value = '';
    document.getElementById('feedbackText').value = '';
  }

</script>
</body>
</html>
