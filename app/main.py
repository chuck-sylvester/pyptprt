# ---------------------------------------------------------------------
# app/main.py
# ---------------------------------------------------------------------
# Run from project root directory:
#      Command: uvicorn app.main:app --reload --port 8000
#   Access via: localhost:8000
#  Stop server: CTRL + C
# ---------------------------------------------------------------------

"""Starting point for Python Patient Portal Reference Application."""

import logging
import os

from fastapi import FastAPI, Request

from app.config import settings
