<p align="center">
   <img src="Image/GeneralYE.png" alt="YouTube Explorer">
</p>
<p align="center">
   <img src="https://img.shields.io/badge/Code_Editor-VS%20Code-blue" alt="Code Editor VS Code">
   <img src="https://img.shields.io/badge/Version-Pre--Release-purple" alt="Version Pre-Release">
   <img src="https://img.shields.io/badge/License-Apache--2.0-red" alt="License Apache-2.0">
   <img src="https://img.shields.io/badge/Python-3.14.0-yellowblue" alt="Python 3.14.0">
</p>

# YouTube Explorer

**YouTube Explorer** is a console-based Python tool for programmatic exploration of YouTube content using **YouTube Data API v3** and **Return YouTube Dislike API**<!-- and **YouTube Transcript API** -->

It is designed for:

- Working within YouTube API quota limits
- Retrieving and filtering comments
- Searching videos and retrieving playlists
- Extracting metadata
- Collecting subtitles

# 🗒️Table of Contents

- [YouTube Explorer](#youtube-explorer)
- [🗒️Table of Contents](#️table-of-contents)
- [❗Requirements](#requirements)
- [❓How to get the YouTube Data API v3 key?](#how-to-get-the-youtube-data-api-v3-key)
- [Core capabilities](#core-capabilities)
  - [🔑YouTube API key handling](#youtube-api-key-handling)
  - [🚪Quota inspection](#quota-inspection)
  - [💌Comment Explorer](#comment-explorer)
  - [📹Video Explorer](#video-explorer)
  - [📈Channel Explorer](#channel-explorer)
  - [🔢Info Explorer](#info-explorer)
- [⚙️ Functionality](#️-functionality)
- [🔧 What do I plan to make in the future?](#-what-do-i-plan-to-make-in-the-future)
- [🖌️License](#️license)
- [❤️Contributing](#️contributing)
  - [🤝How to contribute](#how-to-contribute)
  - [❓Issues](#issues)

# ❗Requirements  

To use YouTube Explorer, you need the following:

1. Your desire to use **YouTube Explorer**
2. A valid YouTube Data API v3 key issued via Google Cloud Console
3. Python 3.10 or newer (required when running from the repository)
4. A stable Internet connection

Basic familiarity with command-line usage is recommended.

# ❓How to get the YouTube Data API v3 key?

1. You need to follow [Google Cloud Console](https://console.cloud.google.com)

2. You need to register for a Google account or log in to it.

3. Next, you press the `Create or select a project` button in the center of the page → `New project`

4. Next, you write the project name (Google can **automatically** specify the name, you do not have to write this name if you want) → If you do not have an organisation, just do not touch the `Location` item. → Press `Create`.

5. Without leaving the site, you need to press `Select project` and choose your project. You write to the search engine: **YouTube Data API v3** → `Enable`

6. You will be redirected to the API configuration. In the left column, you should press `Credentials`.

7. At the top, click `Create credentials` → `API key`.

8. The end of the way! Just copy your API key and paste it into the Windows notepad or somewhere else.

# Core capabilities

## 🔑YouTube API key handling

- Initial validation of the provided API key before execution
- Automatic creation and storage of a `Key.bin` file
- Exclusion of re-entering the key after successful verification

## 🚪Quota inspection

- Detects current availability of the YouTube API quota
- Stops execution if further requests are not possible

## 💌Comment Explorer

- get a list of comments on YouTube videos in the console
- filter comments by keyword
- sort `by time` or `by relevance`
- limit the number of output results
- find out the channel's name where the video is hosted
- Comment Explorer inform why an error occured if it is a cause

## 📹Video Explorer

- Search for videos by your prompt
- Perform region-specific searches
- Apply optional filters such as: `publication date range` and `video duration`
- Control the maximum number of returned search results
- For one video you will receive the information block:
   1. The title of the video
   2. Direct URL
   3. View count
   4. Like count
   5. Dislike count
   6. Comment count
   7. Publication date
   8. Channel name and channel URL

## 📈Channel Explorer

- Collect most of the channel statistics
- If necessary, you can search videos on the channel thanks to Video Explorer

<!-- ## Playlist Explorer

- Get details about a playlist, including the total number of videos
- you can find videos in the certain playlist thanks to Video Explorer

-->

## 🔢Info Explorer

Enter the video URL, and you will receive the information block from Video Explorer. See numbers in [Video Explorer](#video-explorer).

<!-- ## 📄Subtitles Explorer

- You can specify the exact languages for the subtitles you want to collect. Enter one or more two-letter language codes `e.g., en, es, ja` to fetch the corresponding transcripts.
- You need to choose the type of transcript you retrieve. **Manually created** transcripts for higher accuracy. **Auto-generated** transcripts provided by YouTube AI.

-->

# ⚙️ Functionality

- **The API key** from Google Cloud Console (YouTube Data API v3) is being analyzed. If there is an error, it will ask you to enter it again.
- the `video id`, which is required for the YouTube Data API, is extracted from the **YouTube video URL**.
- **Keywords (optional)** — to filter comments. YouTube Explorer will search for comments on these keywords. YouTube Data API will not help it.
- **The sorting method** is `by relevance` or `by time`. If you press Enter, `by relevance` will be entered.
- **Number of comments** — output is limited at the user's request.

# 🔧 What do I plan to make in the future?

- [ ] The ability to save received comments and videos
- [x] Explore the channels
- [x] A more user-friendly, interactive command-line interface
- [ ] Playlist Explorer
- [ ] Subtitles Explorer

# 🖌️License

YouTubeExplorer is licensed under the Apache-2.0 license.

Versions released before 22-01-2026 were licensed under the MIT License.

Author: Valentin Kolesnikov  
Original repository: [YouTube_Explorer](https://github.com/valentin-kolesnikov/YouTube_Explorer)

For more details, see the [LICENSE](LICENSE) and [NOTICE](NOTICE) files.

# ❤️Contributing

Thank you for your interest in contributing to this project.

This project is licensed under the `Apache License, Version 2.0`. By submitting a pull request, you agree that your contribution will be licensed under the `Apache License 2.0`.

If you create a fork or derivative work based on this project, please provide clear attribution in your `README`.

A recommended attribution format is:  
`Original project: YouTube Explorer by Valentin Kolesnikov`

This attribution helps avoid confusion about authorship and is considered good open-source practice.

## 🤝How to contribute

1. Fork the repository.
2. Create a branch for your change.
3. Submit a pull request with a clear description.
4. Make sure your changes are well documented.

## ❓Issues

I will be glad to see your opinions and ideas for new features or improvements. Moreover, please report bugs. Just open an issue and surprise me!