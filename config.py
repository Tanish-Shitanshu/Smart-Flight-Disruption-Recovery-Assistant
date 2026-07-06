"""
Central configuration for the Flight Disruption Recovery Assistant.

All tunable parameters are defined here so they can be changed in one place
without hunting through the codebase.
"""

import os

# ── Database ──────────────────────────────────────────────────────────────────
DB_PATH: str = os.environ.get("FDRА_DB_PATH", "flights.db")

# ── Ranking weights (must sum to 1.0) ─────────────────────────────────────────
SEAT_WEIGHT: float = 0.35
TIME_WEIGHT: float = 0.25
WEATHER_WEIGHT: float = 0.20
CONGESTION_WEIGHT: float = 0.10
RELIABILITY_WEIGHT: float = 0.10

assert abs(SEAT_WEIGHT + TIME_WEIGHT + WEATHER_WEIGHT + CONGESTION_WEIGHT + RELIABILITY_WEIGHT - 1.0) < 1e-9, \
    "Ranking weights must sum to 1.0"

# ── Search defaults ───────────────────────────────────────────────────────────
MAX_ALTERNATIVE_RESULTS: int = 10
MAX_RANKED_RESULTS: int = 3

# ── Risk thresholds ───────────────────────────────────────────────────────────
LOW_RISK_THRESHOLD: float = 0.30
MEDIUM_RISK_THRESHOLD: float = 0.60

# ── OpenSky Network ──────────────────────────────────────────────────────────
OPENSKY_API_URL: str = "https://opensky-network.org/api/states/all"
OPENSKY_TIMEOUT_SECONDS: int = 15

# ── UI ────────────────────────────────────────────────────────────────────────
PAGE_TITLE: str = "✈️ Flight Recovery Assistant"
PAGE_ICON: str = "✈️"
GITHUB_REPO_URL: str = "https://github.com/Tanish-Shitanshu/Smart-Flight-Disruption-Recovery-Assistant"
