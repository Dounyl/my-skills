# Prototype Review Checklist

## Requirement Coverage

- Every named business has its own directory and `overview.html`.
- Every required page and meaningful state appears once.
- Every transition target exists, including branches, loops, failures, and recovery paths.
- No invented feature changes the PRD behavior.

## Visual Output

- Mobile pages use phone frames; desktop pages use browser frames.
- Reference styling is reused when provided.
- Prototype content is the dominant visual; shell controls and callouts stay secondary.
- No PRD summary, page-purpose prose, implementation explanation, or redundant overview description appears.
- Layout remains readable at common laptop widths and browser zoom levels.

## Flow Overview

- Dagre lays out all nodes without overlap.
- Edge direction, labels, and branch colors are legible.
- Every node opens the corresponding page.
- The overview shows relationships rather than a prose transcription of the PRD.

## Editing And Notes

- Editing mode changes text only.
- Notes can be added, moved, edited, completed, and deleted.
- Draft edits survive reload through local storage.
- Saving embeds edits and notes in the HTML snapshot.
- Chrome or Edge can write through a user-selected file handle where supported.
- Unsupported browsers download an updated HTML file.
- The `保存 !` and `重置 !` explanations appear only on demand.
- Reset requires confirmation and restores generated text while removing notes.

## Offline And Files

- No generated HTML references an HTTP or HTTPS script, stylesheet, font, or image unless the user explicitly supplied and accepted it.
- React, ReactDOM, Dagre, runtime JavaScript, and CSS resolve from local files.
- Every page works when opened directly from the filesystem.
- Business directories continue to work when copied independently.

