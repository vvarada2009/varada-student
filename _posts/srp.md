<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Applying SRP to My Code</title>
<style>
  body {
    font-family: Georgia, serif;
    max-width: 800px;
    margin: 60px auto;
    padding: 0 24px;
    font-size: 17px;
    line-height: 1.7;
    color: #222;
    background: #fff;
  }

  h1 { font-size: 2rem; margin-bottom: 8px; }
  h2 { font-size: 1.4rem; margin-top: 52px; margin-bottom: 12px; }
  h3 { font-size: 1.1rem; margin-top: 28px; margin-bottom: 8px; color: #333; }

  p { margin: 0 0 16px; }

  ul { margin: 0 0 16px 0; padding-left: 24px; }
  ul li { margin-bottom: 8px; }

  pre {
    background: #f4f4f4;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 18px 20px;
    overflow-x: auto;
    font-size: 14px;
    line-height: 1.7;
    margin: 16px 0 24px;
  }

  code { font-family: 'Courier New', monospace; }
  p code { background: #f0f0f0; padding: 1px 5px; border-radius: 3px; font-size: 15px; }

  hr { border: none; border-top: 1px solid #ddd; margin: 52px 0; }

  .label {
    display: inline-block;
    font-family: 'Courier New', monospace;
    font-size: 13px;
    font-weight: bold;
    padding: 3px 10px;
    border-radius: 3px;
    margin-bottom: 6px;
  }
  .label-bad  { background: #fde8e8; color: #b00; }
  .label-good { background: #e6f9ee; color: #060; }
</style>
</head>
<body>

<h1>Applying SRP to My Code</h1>
<p>SRP stands for Single Responsibility Principle. The idea is simple: <strong>each function should only do one thing.</strong> If a function is handling three or four different jobs at once, that's a problem — when something breaks or needs to change, you're digging through unrelated code to find it.</p>
<p>Here are two functions from my project where that was happening, and how I fixed them.</p>

<hr>

<h2>Example 1: <code>selectInterChallenge()</code></h2>

<p>This function runs when a student clicks a subject button (Math, Science, etc.) to start a challenge. It sounds like it should do one simple thing, but it was actually handling six completely different jobs at once.</p>

<h3>What it was doing (all in one function):</h3>
<ul>
  <li>Saving which subject the student picked into a variable</li>
  <li>Looping through every button on the page and resetting its color</li>
  <li>Highlighting the selected button</li>
  <li>Clearing the text input and hiding old panels</li>
  <li>Showing the challenge area on screen</li>
  <li>Putting the weak prompt text onto the page</li>
  <li>Resetting the score bar, checkboxes, and feedback area</li>
</ul>

<div class="label label-bad">❌ Before</div>
<pre><code>function selectInterChallenge(subject) {

    // saves state
    currentInterChallenge = subject;
    hintsUsed = 0;

    // restyles all buttons
    document.querySelectorAll('.inter-subject-btn').forEach(btn => {
        btn.classList.remove('bg-orange-600', 'border-orange-500');
        btn.classList.add('bg-slate-700', 'border-slate-600');
    });
    document.getElementById(`inter-${subject}-btn`).classList.add('bg-orange-600', 'border-orange-500');
    document.getElementById(`inter-${subject}-btn`).classList.remove('bg-slate-700', 'border-slate-600');

    // clears inputs and hides panels
    document.getElementById('student-improved-prompt').value = '';
    document.getElementById('hint-display').classList.add('hidden');
    document.getElementById('inter-ai-response').classList.add('hidden');
    document.getElementById('example-answer').classList.add('hidden');

    // shows the challenge section
    document.getElementById('inter-challenge').classList.remove('hidden');

    // displays the weak prompt text
    const challenge = interChallenges[currentInterChallenge];
    document.getElementById('weak-prompt-display').textContent = challenge.weak;

    // resets the score and feedback
    resetAnalysis();
}</code></pre>

<h3>Why this breaks SRP:</h3>
<ul>
  <li>If the button styling breaks, you have to open a function that also handles clearing inputs, showing text, and resetting scores — things that have nothing to do with buttons.</li>
  <li>You can't reuse any of this logic anywhere else in the project because it's all stuck inside one specific function.</li>
  <li>If any one of those jobs causes an error, the whole function stops and nothing works at all.</li>
  <li>It's hard to read — if someone asks "what does this function do?" the honest answer is "everything," which is the whole problem.</li>
</ul>

<div class="label label-good">✅ After</div>
<pre><code>// only saves the current subject
function setCurrentChallenge(subject) {
    currentInterChallenge = subject;
    hintsUsed = 0;
}

// only handles button highlighting
function highlightSubjectButton(subject) {
    document.querySelectorAll('.inter-subject-btn').forEach(btn => {
        btn.classList.remove('bg-orange-600', 'border-orange-500');
        btn.classList.add('bg-slate-700', 'border-slate-600');
    });
    const btn = document.getElementById(`inter-${subject}-btn`);
    btn.classList.add('bg-orange-600', 'border-orange-500');
    btn.classList.remove('bg-slate-700', 'border-slate-600');
}

// only clears the input and hides old panels
function clearChallengeInputs() {
    document.getElementById('student-improved-prompt').value = '';
    document.getElementById('hint-display').classList.add('hidden');
    document.getElementById('inter-ai-response').classList.add('hidden');
    document.getElementById('example-answer').classList.add('hidden');
}

// only puts the weak prompt text on screen
function displayWeakPrompt(subject) {
    document.getElementById('weak-prompt-display').textContent = interChallenges[subject].weak;
}

// coordinator — just calls each small function in order
function selectInterChallenge(subject) {
    setCurrentChallenge(subject);
    highlightSubjectButton(subject);
    clearChallengeInputs();
    displayWeakPrompt(subject);
    resetAnalysis();
    document.getElementById('inter-challenge').classList.remove('hidden');
}</code></pre>

<h3>How this follows SRP:</h3>
<ul>
  <li><strong>Each new function has exactly one job.</strong> <code>highlightSubjectButton()</code> only touches button colors. <code>clearChallengeInputs()</code> only resets the form. They don't know about each other and don't interfere.</li>
  <li><strong>Easier to fix bugs.</strong> If button highlighting breaks, you go straight to <code>highlightSubjectButton()</code>. You don't have to scroll through 30 lines of unrelated code to find the problem.</li>
  <li><strong>Functions are now reusable.</strong> <code>clearChallengeInputs()</code> can be called from anywhere else in the project that needs to reset the form. Before, that logic was trapped and couldn't be reused.</li>
  <li><strong>The coordinator function stays clean.</strong> <code>selectInterChallenge()</code> still exists but now it just calls the smaller functions in order. You can read it like a checklist and immediately understand what happens when a student picks a subject.</li>
</ul>

<hr>

<h2>Example 2: <code>analyzeStudentPrompt()</code></h2>

<p>This runs every time the student types in the text box. It's supposed to score their prompt and give live feedback. But it was doing three totally different things — calculating a score, updating the visual bar on screen, and writing feedback messages — all tangled together in one place.</p>

<h3>What it was doing (all in one function):</h3>
<ul>
  <li>Checking the student's text against a list of keywords to calculate a score out of 100</li>
  <li>Updating the score bar's width and color on the screen based on that score</li>
  <li>Building a list of feedback messages and writing them to the page</li>
</ul>

<div class="label label-bad">❌ Before</div>
<pre><code>function analyzeStudentPrompt() {
    const studentPrompt = document.getElementById('student-improved-prompt').value.trim();

    if (!studentPrompt) { resetAnalysis(); return; }

    const challenge   = interChallenges[currentInterChallenge];
    const lowerPrompt = studentPrompt.toLowerCase();

    // scoring logic
    let score = 0;
    let checks = { specificity: false, context: false, detail: false, length: false };

    if (challenge.keywords.specific.some(kw => lowerPrompt.includes(kw))) { checks.specificity = true; score += 25; }
    if (challenge.keywords.context.some(kw  => lowerPrompt.includes(kw))) { checks.context     = true; score += 25; }
    if (challenge.keywords.detail.some(kw   => lowerPrompt.includes(kw))) { checks.detail      = true; score += 25; }
    if (studentPrompt.length > 50)                                         { checks.length      = true; score += 25; }

    updateCheck('check-specificity', checks.specificity);
    updateCheck('check-context',     checks.context);
    updateCheck('check-detail',      checks.detail);
    updateCheck('check-length',      checks.length);

    // score bar update mixed in right after
    document.getElementById('quality-score').textContent = score + '%';
    document.getElementById('quality-bar').style.width = score + '%';
    if (score >= 75) {
        document.getElementById('quality-bar').className = 'bg-green-500 h-4 rounded-full transition-all duration-500';
    } else if (score >= 50) {
        document.getElementById('quality-bar').className = 'bg-yellow-500 h-4 rounded-full transition-all duration-500';
    } else {
        document.getElementById('quality-bar').className = 'bg-red-500 h-4 rounded-full transition-all duration-500';
    }

    // feedback messages crammed in at the bottom
    let feedback = [];
    if (!checks.specificity) feedback.push("❌ Add more specific details about the topic");
    if (!checks.context)     feedback.push("❌ Provide context about yourself and your purpose");
    if (!checks.detail)      feedback.push("❌ Specify what details you want included");
    if (!checks.length)      feedback.push("❌ Your prompt is too short");
    if (score === 100) feedback = ["✅ Excellent! Your prompt looks great!"];

    document.getElementById('feedback-display').innerHTML = feedback.map(f => `&lt;p&gt;${f}&lt;/p&gt;`).join('');
}</code></pre>

<h3>Why this breaks SRP:</h3>
<ul>
  <li>The math that calculates the score is mixed in with code that draws things on screen. Those are two completely different jobs — one is logic, one is visual.</li>
  <li>If you want to change the colors on the score bar, you have to scroll past all the keyword-checking code just to find the right lines.</li>
  <li>You can't verify whether the scoring is correct on its own — to run it, you also have to run all the screen-update code, which requires a browser and an actual HTML page.</li>
  <li>This fires on every single keystroke. If anything in the function is broken, the whole feedback panel stops working.</li>
</ul>

<div class="label label-good">✅ After</div>
<pre><code>// only calculates the score — no screen updates at all
function scorePrompt(promptText, subject) {
    const challenge   = interChallenges[subject];
    const lowerPrompt = promptText.toLowerCase();

    const checks = {
        specificity: challenge.keywords.specific.some(kw => lowerPrompt.includes(kw)),
        context:     challenge.keywords.context.some(kw  => lowerPrompt.includes(kw)),
        detail:      challenge.keywords.detail.some(kw   => lowerPrompt.includes(kw)),
        length:      promptText.length > 50
    };

    const score = Object.values(checks).filter(Boolean).length * 25;
    return { checks, score }; // just returns data, doesn't touch the screen
}

// only updates the score bar color and percentage
function renderScoreBar(score) {
    document.getElementById('quality-score').textContent = score + '%';
    document.getElementById('quality-bar').style.width = score + '%';

    if (score >= 75) {
        document.getElementById('quality-bar').className = 'bg-green-500 h-4 rounded-full transition-all duration-500';
    } else if (score >= 50) {
        document.getElementById('quality-bar').className = 'bg-yellow-500 h-4 rounded-full transition-all duration-500';
    } else {
        document.getElementById('quality-bar').className = 'bg-red-500 h-4 rounded-full transition-all duration-500';
    }
}

// only builds and writes the feedback messages
function renderFeedback(checks, score) {
    let feedback = [];
    if (!checks.specificity) feedback.push("❌ Add more specific details about the topic");
    if (!checks.context)     feedback.push("❌ Provide context about yourself and your purpose");
    if (!checks.detail)      feedback.push("❌ Specify what details you want included");
    if (!checks.length)      feedback.push("❌ Your prompt is too short - add more information");
    if (score === 100)        feedback = ["✅ Excellent! Your prompt looks great!"];

    document.getElementById('feedback-display').innerHTML = feedback.map(f => `&lt;p&gt;${f}&lt;/p&gt;`).join('');
}

// coordinator — reads the input, hands work off to each function
function analyzeStudentPrompt() {
    const promptText = document.getElementById('student-improved-prompt').value.trim();

    if (!promptText) { resetAnalysis(); return; }

    const { checks, score } = scorePrompt(promptText, currentInterChallenge);

    updateCheck('check-specificity', checks.specificity);
    updateCheck('check-context',     checks.context);
    updateCheck('check-detail',      checks.detail);
    updateCheck('check-length',      checks.length);

    renderScoreBar(score);
    renderFeedback(checks, score);
}</code></pre>

<h3>How this follows SRP:</h3>
<ul>
  <li><strong><code>scorePrompt()</code> is pure logic with no screen updates.</strong> It takes in text and a subject name, checks keywords, and just returns a score and a set of true/false values. Because it doesn't touch the screen at all, you could test it by just calling it with a string — no browser or HTML needed.</li>
  <li><strong><code>renderScoreBar()</code> only cares about the bar.</strong> If the design changes and you want different colors or a different style, this is the only function you need to touch. Nothing else is affected.</li>
  <li><strong><code>renderFeedback()</code> only handles messages.</strong> If you want to reword any of the feedback text, it's all in one place. You don't have to search through scoring logic to find it.</li>
  <li><strong>The coordinator just connects everything.</strong> <code>analyzeStudentPrompt()</code> now just reads the input, calls <code>scorePrompt()</code>, and passes the result to the two render functions. It doesn't do any of that work itself — it just coordinates.</li>
  <li><strong>The biggest win here</strong> is that the scoring logic and the screen-drawing code are now completely separate. Before, they were the same thing. Mixing logic and visuals in the same function is one of the most common SRP violations, and this fixes it cleanly.</li>
</ul>

</body>
</html>
