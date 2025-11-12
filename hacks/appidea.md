---
layout: base
title: Snake Game
permalink: /app/
---


```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ease - Elder Care Companion</title>

<!-- ================== CSS ================== -->
<style>
  /* --- Global Styles --- */
  body {
    font-family: "Segoe UI", Arial, sans-serif;
    margin: 0;
    background-color: #f0f7f6;
    color: #333;
  }

  header {
    text-align: center;
    background: linear-gradient(135deg, #4caf50, #81c784);
    color: white;
    padding: 25px 10px;
  }
  header h1 { margin: 0; font-size: 2em; }
  header p { margin: 5px 0 0 0; font-size: 1em; }

  /* --- Sections / Cards --- */
  section {
    display: none;
    padding: 20px;
    max-width: 600px;
    margin: 100px auto 100px auto;
    background-color: #ffffff;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
  }
  section.active { display: block; }

  h2 {
    margin-top: 0;
    color: #4caf50;
    text-align: center;
  }

  textarea, input[type="text"], input[type="time"] {
    width: 100%;
    padding: 12px;
    margin: 5px 0 15px 0;
    border-radius: 10px;
    border: 1px solid #ccc;
    font-size: 1em;
  }

  button.submit-btn {
    padding: 12px 20px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-size: 1em;
    margin-bottom: 15px;
    width: 100%;
    transition: 0.2s;
  }
  button.submit-btn:hover { background-color: #45a049; }

  ul { list-style: none; padding: 0; }
  li {
    background-color: #e8f5e9;
    padding: 10px;
    margin: 8px 0;
    border-radius: 8px;
  }

  /* --- Bottom Tab Navigation --- */
  nav {
    display: flex;
    justify-content: space-around;
    background-color: #ffffff;
    border-top: 1px solid #ccc;
    position: fixed;
    bottom: 0;
    width: 100%;
    padding: 10px 0;
    box-shadow: 0 -2px 6px rgba(0,0,0,0.1);
    z-index: 1000;
  }

  nav button {
    background: none;
    border: none;
    font-size: 0.9em;
    cursor: pointer;
    color: #555;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  nav button.active { color: #4caf50; font-weight: bold; }

  /* --- Responsive --- */
  @media (max-width: 600px) {
    header h1 { font-size: 1.8em; }
    header p { font-size: 0.9em; }
    nav button { font-size: 0.8em; }
  }

</style>
</head>

<body>

<header>
  <h1>Ease</h1>
  <p>Daily Care & Pain Tracking for Seniors</p>
</header>

<!-- ================== Sections ================== -->
<section id="home" class="active">
  <h2>Welcome to Ease!</h2>
  <p>This app helps seniors manage pain, medications, exercises, and family involvement. Simple, mobile-friendly, and polished for real use.</p>
  <ul>
    <li>Log daily pain and symptoms</li>
    <li>Add and track medication reminders</li>
    <li>Track exercises and mobility routines</li>
    <li>Share updates with family members (Care Circle)</li>
  </ul>
</section>

<section id="pain-log">
  <h2>Pain Log</h2>
  <textarea id="pain-input" placeholder="Describe your pain today..."></textarea>
  <input type="text" id="pain-tags" placeholder="Optional: Body part(s), intensity (e.g., knee, 6/10)">
  <button class="submit-btn" onclick="addPainEntry()">Add Entry</button>
  <ul id="pain-list"></ul>
</section>

<section id="medications">
  <h2>Medication Reminder</h2>
  <input type="text" id="med-name" placeholder="Medication Name">
  <input type="text" id="med-dosage" placeholder="Dosage (e.g., 200mg)">
  <input type="time" id="med-time">
  <button class="submit-btn" onclick="addMedication()">Add Medication</button>
  <ul id="med-list"></ul>
</section>

<section id="exercises">
  <h2>Exercises & Mobility</h2>
  <input type="text" id="exercise-name" placeholder="Exercise Name (e.g., Knee Stretch)">
  <input type="text" id="exercise-time" placeholder="Recommended Duration/Time">
  <button class="submit-btn" onclick="addExercise()">Add Exercise</button>
  <ul id="exercise-list"></ul>
</section>

<section id="care-circle">
  <h2>Care Circle</h2>
  <p>Family and caregivers can add notes for the patient.</p>
  <input type="text" id="family-note" placeholder="Add a note for your loved one">
  <button class="submit-btn" onclick="addFamilyNote()">Add Note</button>
  <ul id="family-list"></ul>
</section>

<!-- ================== Navigation Tabs ================== -->
<nav>
  <button class="tab-btn active" onclick="openTab('home', event)">Home</button>
  <button class="tab-btn" onclick="openTab('pain-log', event)">Pain Log</button>
  <button class="tab-btn" onclick="openTab('medications', event)">Medications</button>
  <button class="tab-btn" onclick="openTab('exercises', event)">Exercises</button>
  <button class="tab-btn" onclick="openTab('care-circle', event)">Care Circle</button>
</nav>

<!-- ================== JavaScript ================== -->
<script>
  // ----------------- Tab Navigation -----------------
  function openTab(tabId, event){
    document.querySelectorAll('section').forEach(s => s.classList.remove('active'));
    document.getElementById(tabId).classList.add('active');
    document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
    event.currentTarget.classList.add('active');
  }

  // ----------------- Load Persistent Data -----------------
  window.onload = function() {
    loadPainLogs();
    loadMedications();
    loadExercises();
    loadFamilyNotes();
  }

  // ----------------- Pain Log -----------------
  function addPainEntry(){
    const input = document.getElementById('pain-input').value;
    const tags = document.getElementById('pain-tags').value;
    if(!input){ alert("Please enter pain description."); return; }

    const entry = { text: input, tags: tags, timestamp: new Date().toLocaleString() };
    let logs = JSON.parse(localStorage.getItem('painLogs')) || [];
    logs.push(entry);
    localStorage.setItem('painLogs', JSON.stringify(logs));
    displayPainLog(entry);
    document.getElementById('pain-input').value = '';
    document.getElementById('pain-tags').value = '';
  }
  function displayPainLog(entry){
    const li = document.createElement('li');
    li.textContent = `${entry.timestamp}: ${entry.text}` + (entry.tags ? ` (${entry.tags})` : '');
    document.getElementById('pain-list').appendChild(li);
  }
  function loadPainLogs(){
    let logs = JSON.parse(localStorage.getItem('painLogs')) || [];
    logs.forEach(displayPainLog);
  }

  // ----------------- Medications -----------------
  function addMedication(){
    const name = document.getElementById('med-name').value;
    const dose = document.getElementById('med-dosage').value;
    const time = document.getElementById('med-time').value;
    if(!name || !dose || !time){ alert("Please fill all fields."); return; }

    const med = { name, dose, time };
    let meds = JSON.parse(localStorage.getItem('medications')) || [];
    meds.push(med);
    localStorage.setItem('medications', JSON.stringify(meds));
    displayMedication(med);
    document.getElementById('med-name').value = '';
    document.getElementById('med-dosage').value = '';
    document.getElementById('med-time').value = '';
  }
  function displayMedication(med){
    const li = document.createElement('li');
    li.textContent = `${med.name} - ${med.dose} at ${med.time}`;
    document.getElementById('med-list').appendChild(li);
  }
  function loadMedications(){
    let meds = JSON.parse(localStorage.getItem('medications')) || [];
    meds.forEach(displayMedication);
  }

  // ----------------- Exercises -----------------
  function addExercise(){
    const name = document.getElementById('exercise-name').value;
    const duration = document.getElementById('exercise-time').value;
    if(!name || !duration){ alert("Please fill all fields."); return; }

    const exercise = { name, duration };
    let exercises = JSON.parse(localStorage.getItem('exercises')) || [];
    exercises.push(exercise);
    localStorage.setItem('exercises', JSON.stringify(exercises));
    displayExercise(exercise);
    document.getElementById('exercise-name').value = '';
    document.getElementById('exercise-time').value = '';
  }
  function displayExercise(exercise){
    const li = document.createElement('li');
    li.textContent = `${exercise.name} - ${exercise.duration}`;
    document.getElementById('exercise-list').appendChild(li);
  }
  function loadExercises(){
    let exercises = JSON.parse(localStorage.getItem('exercises')) || [];
    exercises.forEach(displayExercise);
  }

  // ----------------- Care Circle -----------------
  function addFamilyNote(){
    const note = document.getElementById('family-note').value;
    if(!note){ alert("Please enter a note."); return; }

    const noteObj = { text: note, timestamp: new Date().toLocaleString() };
    let notes = JSON.parse(localStorage.getItem('familyNotes')) || [];
    notes.push(noteObj);
    localStorage.setItem('familyNotes', JSON.stringify(notes));
    displayFamilyNote(noteObj);
    document.getElementById('family-note').value = '';
  }
  function displayFamilyNote(noteObj){
    const li = document.createElement('li');
    li.textContent = `${noteObj.timestamp}: ${noteObj.text}`;
    document.getElementById('family-list').appendChild(li);
  }
  function loadFamilyNotes(){
    let notes = JSON.parse(localStorage.getItem('familyNotes')) || [];
    notes.forEach(displayFamilyNote);
  }

</script>

</body>
</html>

