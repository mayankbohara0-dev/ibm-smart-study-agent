# Smart Study Agent

**Smart Study Agent** is a single-page AI learning hub designed to help students organize study sessions and practice concepts from one focused workspace. The repository is a self-contained HTML prototype with a dark, responsive interface and client-side interactions for study planning, revision, and AI-assisted learning.

The page is branded as **SmartStudy** and includes an embedded IBM Watsonx Orchestrate chat experience for the AI assistant area. Other modules are implemented as front-end demonstration flows with local in-page state and sample learning data.

## Features

| Module | What it provides |
| --- | --- |
| AI Assistant | A Watson AI study-assistant area for questions, explanations, and quick prompts |
| Subject Hub | Subject selection, subject cards, progress indicators, and learning statistics |
| Notes & Files | A file drop zone and analysis-result presentation for study material workflows |
| AI Summaries | Summary views with visual mind-map and audio-player presentation modes |
| 3D Flashcards | Flip-based flashcards for active recall practice |
| Smart Quiz | Timed multiple-choice quiz flow with answer states and explanations |
| Planner & Timer | Weekly study schedule, task checklist, and Pomodoro-style focus timer |
| Gamification | Study streak, XP, weekly target, and progress-oriented UI elements |
| Theme support | Dark theme by default with a light-theme toggle |

## Technology and design

| Area | Implementation |
| --- | --- |
| Application format | Static HTML document with inline CSS and JavaScript |
| External service | IBM Watsonx Orchestrate chat loader embedded in the page |
| Typography | Outfit and Plus Jakarta Sans from Google Fonts |
| Visual style | Dark dashboard, gradient accents, glassmorphism, responsive cards, and animated transitions |
| Responsive behavior | Desktop sidebar layout that collapses into a horizontal navigation layout on smaller screens |
| Data model | Demonstration data and UI state held in the browser; no local backend is included |

## Repository structure

```text
.
├── index.html    Complete SmartStudy interface, styles, module markup, and client-side behavior
└── README.md     Project documentation
```

## Run locally

Because the project is a static page, it can be previewed directly in a browser or served with any static HTTP server.

```bash
git clone https://github.com/mayankbohara0-dev/ibm-smart-study-agent.git
cd ibm-smart-study-agent

# Option 1: open index.html directly
# Option 2: serve it locally with Python
python3 -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000) after starting the local server. A static server is recommended because it mirrors normal web hosting behavior and avoids browser restrictions that can affect embedded resources.

## IBM Watsonx Orchestrate configuration

The page contains a `window.wxOConfiguration` object with the Watsonx Orchestrate host URL, orchestration identifier, root element identifier, and agent identifier. The loader script is inserted dynamically and mounts the assistant into the `#root` element.

Before deploying a public copy, confirm that the referenced Watsonx Orchestrate deployment is intended to be public, that its access policy is correct, and that environment-specific identifiers are not being exposed unintentionally. If the embedded assistant is unavailable, the rest of the static prototype remains useful as a front-end demonstration.

## Development notes

The current implementation is intentionally self-contained: styles and scripts are embedded in `index.html`, and many study values, questions, flashcards, and progress metrics are demonstration data. A production implementation would normally split the interface into components, connect the analyzer and summaries to a secured backend, persist user progress, validate uploaded files server-side, and add accessibility and automated browser tests.

## License

No license file is currently included. Add a `LICENSE` file if you want to define how others may use, modify, and redistribute the project.

## Author

Maintained by [Mayank Bohara](https://github.com/mayankbohara0-dev).

## References

[1]: https://github.com/mayankbohara0-dev/ibm-smart-study-agent "Smart Study Agent repository"
[2]: https://www.ibm.com/products/watsonx-orchestrate "IBM watsonx Orchestrate"
