# 🎥 AI Video Interview Trainer (Notebook)

An end-to-end **multimodal AI video interview trainer** implemented as a single Jupyter notebook + small helper modules.  
This project replicates a realistic interview experience by:

- Generating **progressive interview questions** (Easy → Medium → Hard) using your **Job Title**, **Job Description**, and **Résumé** (OpenAI).
- Capturing **video-only** (webcam) and **audio-only** (microphone) answers, merging them into synchronized final clips (MoviePy).
- Transcribing answers (Whisper), performing forced-alignment (MFA) for precise timings, extracting acoustic & visual embeddings (WavLM, VideoMAE), and predicting **confidence** with a multimodal classifier.
- Producing **two kinds of feedback** per answer:
  1. **Answer-quality feedback**: positive/negative/missing points + a model answer tailored to your background.
  2. **Delivery feedback**: WPM, filler ratio, pauses, fluency tips (MFA + acoustic metrics).
- Saving outputs (videos, transcripts, metrics, feedback JSON) in a structured `outputs/` folder.

> This README provides **complete, step-by-step instructions** to run the notebook locally, install requirements, configure MFA & FFmpeg, and reproduce the pipeline exactly like the audio-interview repo you used before.

---

## 📚 Table of Contents

- [Overview](#-overview)  
- [Features](#-features)  
- [System Architecture (Diagram & Flow)](#-system-architecture-diagram--flow)  
- [Quick Start (Local)](#-quick-start-local)  
- [Repository Structure](#-repository-structure)  
- [Requirements](#-requirements)  
  - [1) Python & OS](#1-python--os)  
  - [2) Python Packages](#2-python-packages)  
  - [3) External Tools](#3-external-tools)  
  - [4) Environment Variables / PATH](#4-environment-variables--path)  
  - [5) API Keys](#5-api-keys)  
- [Download the Code](#-download-the-code)  
- [Run (Notebook & Script)](#-run-notebook--script)  
- [Config You May Need to Edit](#-config-you-may-need-to-edit)  
- [Outputs (What the pipeline saves)](#-outputs-what-the-pipeline-saves)  
- [Optional: MFA Alignment Setup (Detailed)](#-optional-mfa-alignment-setup-detailed)  
- [Troubleshooting (Common errors & fixes)](#-troubleshooting-common-errors--fixes)  
- [Security Note](#-security-note)  
- [Sample requirements.txt](#-sample-requirementstxt)  
- [Demonstration & Gallery](#-demonstration--gallery)

---

## 🔎 Overview

This notebook (`Video_Interview_trainer.ipynb`) implements a full interview pipeline:

1. Accepts inputs: **Job Title**, **Job Description**, **Résumé**, **Interview type**, **Experience level**.
2. Uses **OpenAI** to generate a sequence of progressive questions tailored to the inputs.
3. For each question:
   - Displays the question (OpenCV window / console).
   - Records **video-only** (webcam) for the user's answer.
   - Records **audio-only** (microphone) for the same answer.
   - Merges audio + video using **MoviePy** into `mp4`.
   - Runs **Whisper** to transcribe answer.
   - Runs **MFA** (Montréal Forced Aligner) for precise word timings.
   - Extracts audio embeddings (**WavLM**) and video embeddings (**VideoMAE**).
   - Runs a multimodal **confidence classifier** (your trained PyTorch model) to predict `confident/moderately confident/not confident`.
   - Computes delivery metrics: WPM, filler ratio, silence distribution.
   - Calls **OpenAI** to generate answer-quality feedback and suggested model answer using the transcript + candidate info + question.
4. Stores everything in `outputs/` and prints/saves a JSON summary.

---

## ✨ Features

- Question generation: LLM-crafted progressive difficulty (easy → medium → hard).  
- Video capture: OpenCV-based webcam capture with configurable resolution & FPS.  
- Audio capture: `sounddevice` high-quality recording with resampling to 16kHz for models.  
- Merge: MoviePy merges audio/video and handles codecs (H.264 / AAC).  
- Transcription: OpenAI Whisper (choose model size for speed/accuracy).  
- Forced alignment: Montreal Forced Aligner (MFA) for word-level timestamps → precise pause/filler computation.  
- Acoustic features: WavLM (Hugging Face) for audio embeddings.  
- Visual features: VideoMAE for frame embeddings.  
- Confidence prediction: PyTorch model combining audio + visual features.  
- Feedback: LLM-generated content & delivery suggestions.  
- Outputs: final mp4, transcript txt, feedback JSON, metrics CSV/JSON.

---

## 🧠 System Architecture (Diagram & Flow)

### ASCII Flow Diagram

+------------------+
| User Inputs | (Job title, JD, Resume, Interview type)
+--------+---------+
|
v
+------------------+
| Question Generator|
| (OpenAI GPT) |
+--------+---------+
|
v
+-----------------------------+
| Interview Loop (per question)|
+-----------------------------+
| 1) Show Question |
| 2) Record video-only (cv2) |
| 3) Record audio-only (sd) |
| 4) Merge A+V (moviepy) |
| 5) ASR (whisper) |
| 6) MFA alignment |
| 7) Feature extraction |
| - Audio: WavLM |
| - Video: VideoMAE |
| 8) Confidence classifier |
| 9) LLM Feedback generation |
+-----------------------------+
|
v
+------------------+
| Outputs & Reports |
+------------------+
