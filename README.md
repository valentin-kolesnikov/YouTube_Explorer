<p align="center">
   <img src="Image/GeneralYE.png" alt="YouTube Explorer">
</p>
<p align="center">
   <img src="https://img.shields.io/badge/Code_Editor-VS%20Code-blue" alt="Code Editor VS Code">
   <img src="https://img.shields.io/badge/Version-1.0v-purple" alt="Version 1.0v">
   <img src="https://img.shields.io/badge/License-Apache--2.0-red" alt="License Apache-2.0">
   <img src="https://img.shields.io/badge/Python-3.14+-yellowblue" alt="Python 3.14+">
</p>

## <p align="center">English | <a href="README_RU.md">Русский</a></p>

**YouTube Explorer** is a console-based Python tool for programmatic exploration of YouTube content using **YouTube Data API v3** (with OAuth 2.0 support), **Return YouTube Dislike API**, and **YouTube Transcript API**

> [!CAUTION]
> The original repository is only available in my [GitHub](https://github.com/valentin-kolesnikov/YouTube_Explorer) repository  
> Clones, distributed on my behalf on other websites and **GitHub** repositories, are not my work.

> [!WARNING]
> Antivirus software reacts to the app as a potentially unwanted app. This is clearly an error.  
> All materials used for the app are stored in the public repository.  
> As a developer, I have no desire to harm other users. You can always contact me via email for such issues.

YouTube Explorer is designed for:

- Working within YouTube API quota limits
- Retrieving and filtering comments
- Searching videos and retrieving playlists
- Extracting metadata
- Collecting subtitles

# 🗒️Table of Contents

- [🗒️Table of Contents](#️table-of-contents)
- [❗Requirements](#requirements)
- [🌐How to download?](#how-to-download)
  - [Releases](#releases)
  - [Git](#git)
  - [Linux](#linux)
- [❓How to get the YouTube Data API v3 key?](#how-to-get-the-youtube-data-api-v3-key)
- [🛡️ How to get OAuth 2.0 credentials?](#️-how-to-get-oauth-20-credentials)
- [Core capabilities](#core-capabilities)
  - [🔑YouTube API key handling](#youtube-api-key-handling)
  - [🚪Quota inspection](#quota-inspection)
  - [💌Comment Explorer](#comment-explorer)
  - [📹Video Explorer](#video-explorer)
  - [📈Channel Explorer](#channel-explorer)
  - [🗂️Playlist Explorer](#️playlist-explorer)
  - [📄Subtitles Explorer](#subtitles-explorer)
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

# 🌐How to download?

## Releases

1. `Releases` → `YouTubeExplorer.zip`
2. Extract the `.zip` folder
3. `bin` → open `YouTubeExplorer.exe`

The binary works on Windows, not on Linux without `Wine` (a compatibility layer capable of running Windows applications).

## Git

`git clone https://github.com/valentin-kolesnikov/YouTube_Explorer`

## Linux

`curl -L -o YouTubeExplorer.zip https://github.com/valentin-kolesnikov/YouTube_Explorer/releases/download/v0.9.0/YouTubeExplorer.zip`

You download the repository with the code. You need to download `Python 3.10+`. It need more for Linux users, unfortunately.

# ❓How to get the YouTube Data API v3 key?

1. You need to follow [Google Cloud Console](https://console.cloud.google.com)

2. You need to register for a Google account or log in to it.

3. Next, you press the `Create or select a project` button in the center of the page → `New project`

4. Next, you write the project name (Google can **automatically** specify the name, you do not have to write this name if you want) → If you do not have an organisation, just do not touch the `Location` item. → Press `Create`.

5. Without leaving the site, you need to press `Select project` and choose your project. You write to the search engine: **YouTube Data API v3** → `Enable`

6. You will be redirected to the API configuration. In the left column, you should press `Credentials`.

7. At the top, click `Create credentials` → `API key`.

8. The end of the way! Just copy your API key and paste it into the Windows notepad or somewhere else.

# 🛡️ How to get OAuth 2.0 credentials?

- The application is designed to use **OAuth 2.0** as the primary authentication method
- If OAuth client secrets are not found, the system switches to the **YouTube Data API Key** method without interrupting the user
- There is a problem registering the application in OAuth 2, so we create credentials ourselves.

How to set it up:

1. Go to the [Google Cloud Console](https://console.cloud.google.com).

2. Select the project you already created for your YouTube Data API v3 key.

3. In the left column, click `OAuth consent screen`.

4. Choose `External` as the User Type and click `Create`.

5. Fill in the required fields: **App name**, **User support email**, and **Developer contact information** (you can just use your own email for all of these). Click `Save and Continue`.

6. You can skip the **Scopes** page by clicking `Save and Continue`.

7. On the **Test users** page, click `Add Users` and type in your own Google account email. Click `Save and Continue`.

8. Now, click on `Credentials` in the left column again.

9. At the top, click `Create credentials` → `OAuth client ID`.

10. Select `Desktop app` as the Application type. You can leave the default name. Click `Create`.

11. A window will pop up. Click `Download JSON` to save your credentials.

12. The downloaded `.json` file must be placed in the `Keys` folder of the `bin` folder.

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

- Collect most of the channel statistics:
  - subscriber count  
  - view count  
  - description  
  - registration date
  - Channel ID (UC...)
  - Handle (@...)
- If necessary, you can search videos on the channel thanks to Video Explorer

## 🗂️Playlist Explorer

- Search for playlists using keywords, or securely load **your own** playlists using OAuth 2.0
- View basic playlist details, such as privacy status, total video count, and publication date
- Easily extract all videos from any playlist by entering its URL (supports both `PL...` and `OL...` links)
- Get detailed statistics for every video inside the playlist, complete with dislike counts
- Analyze a playlist's video library right after finding it, without needing to go back to the main menu

## 📄Subtitles Explorer

- **Subtitles Explorer** makes extracting text from videos effortless and flexible. You simply enter the two-letter language codes, such as `en` or `ru`
- It gives you the choice between `manually created` subtitles for better accuracy or `auto-generated` transcripts. The system is designed to handle missing data intelligently
- If your preferred transcript type is not available, it will not just show an error and stop. Instead, it detects the issue and offers the alternative version immediately, ensuring you can still retrieve the content you are looking for.

## 🔢Info Explorer

- Enter a specific video URL to directly extract metadata without searching
- Returns the complete information block detailed in [Video Explorer](#video-explorer) and, additionally, the video description

# ⚙️ Functionality

- **Authentication** — **OAuth 2.0** is prioritized for secure access. If OAuth credentials are not detected, the application uses the **YouTube Data API key** stored in `Key.bin`
- **Link parsing** — `video id`, `channel id` (UC...), and `handle` (@...) are automatically extracted from the links you enter
- **Search filters** — you can filter videos by `Region`, `Dimension` (2D or 3D), `Duration`, and `Date` (using the smart calendar)
- **Channel search** — unlike standard search, you can perform keyword searches specifically inside a channel's library
- **Smart Subtitles** — **YouTube Transcript API** is integrated. It looks for `manually created` subtitles first. If they are missing, it asks if you want `auto-generated` ones
- **Dislikes** — **Return YouTube Dislike API** is integrated to show dislike counts mixed with official data
- **Comment filtering** — **Keywords** are used to filter comments and replies locally. YouTube Data API does not do this filtering
- **Quota check** — a test request is made at the start to ensure your **YouTube API quota** is not exceeded before running
- **Automatic verification** — before making API requests, YouTube Explorer pings `google.com` to ensure your connection is active. If the connection lost, you can retry to connect

# 🔧 What do I plan to make in the future?

- [ ] The ability to save received comments and videos

# 🖌️License

YouTube Explorer is licensed under the `Apache-2.0 license`.

Versions released before 22-01-2026 were licensed under the `MIT License`.

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
 
<!-- ## Striving

Probably soon I will stop updating YouTube Explorer. I need to gain experience in different areas. I must grow even more! -->