# Smart Study Agent

**Smart Study Agent** is a self-contained single-page AI learning hub for organizing study sessions and practicing concepts from one focused workspace. It combines a responsive dashboard with an embedded IBM watsonx Orchestrate assistant area and front-end demonstrations of common study workflows.

## Features

- AI assistant area for questions, explanations, and quick prompts.
- Subject hub with progress indicators and learning statistics.
- Notes and files drop zone with analysis-result presentation.
- AI summary views with mind-map and audio-player modes.
- Flip-based flashcards, timed quizzes, explanations, and answer states.
- Weekly planner, checklist, Pomodoro-style timer, streaks, XP, and theme toggle.

## Technology and design

| Area | Implementation |
| --- | --- |
| Application | Static HTML document with inline CSS and JavaScript |
| AI integration | IBM watsonx Orchestrate chat loader |
| Visual system | Responsive dark dashboard, glassmorphism, gradient accents, and animated transitions |
| Data | Demonstration data and browser-local UI state |

## Run locally

```bash
git clone https://github.com/mayankbohara0-dev/ibm-smart-study-agent.git
cd ibm-smart-study-agent
python3 -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000). Opening `index.html` directly is also possible, but a local server better reflects normal hosting behavior.

## Configuration and scope

The Watsonx configuration is embedded in `index.html`. Before deploying publicly, confirm that the referenced deployment is intended to be public and that its access policy is appropriate. Many study values and interactions are demonstration data; a production version would add a secured backend, persistent progress, server-side file validation, accessibility coverage, and automated browser tests.

## Author

Maintained by [Mayank Bohara](https://github.com/mayankbohara0-dev).
