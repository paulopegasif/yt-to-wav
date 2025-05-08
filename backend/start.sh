#!/bin/bash
pip install -U yt-dlp #update 
uvicorn main:app --host 0.0.0.0 --port $PORT