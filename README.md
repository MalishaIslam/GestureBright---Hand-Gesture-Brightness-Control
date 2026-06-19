# ✋ GestureBright — Hand Gesture Brightness Control

Control your laptop screen brightness with just your fingers — no keyboard, no buttons, just your hand in front of a webcam.

---

## 🧠 How It Works

The app uses your webcam to detect hand landmarks in real time using **MediaPipe**. It measures the distance between your **thumb tip** (landmark 4) and **index fingertip** (landmark 8), then maps that distance to a brightness level (0–100%) using `screen_brightness_control`.

Pinch your fingers close → dim the screen.  
Spread them apart → increase brightness.

A visual bar on the screen shows the current brightness level as you move your hand.

---

## 📁 Project Structure

```
GestureBright/
│
├── handtip_detect_brightness_control.py  # Main app — hand detection + brightness control
├── brightness_control.py                 # Alternate version with volume/brightness toggle
├── handpart.py                           # Reusable hand detector module (class-based)
└── blabla.py                             # Scratchpad / experimental tests
```

### File Overview

| File | Purpose |
|------|---------|
| `handtip_detect_brightness_control.py` | Primary script — uses MediaPipe directly, controls brightness via thumb-index distance |
| `brightness_control.py` | Modular version — uses `handpart.py` class, supports both volume (pycaw) and brightness (sbc) |
| `handpart.py` | Reusable `handdetector` class with `findhands()` and `findpos()` methods |
| `blabla.py` | Scratch file for testing `screen_brightness_control` and early experiments |

---

## 🛠️ Requirements

**Python 3.7+**

Install dependencies:

```bash
pip install opencv-python mediapipe screen-brightness-control numpy pyttsx3
```

For the volume control variant (`brightness_control.py`):

```bash
pip install pycaw comtypes
```

> **Note:** `pycaw` and `winsound` are Windows-only. The main brightness control script works cross-platform.

---

## 🚀 Usage

Run the main script:

```bash
python handtip_detect_brightness_control.py
```

- Hold your hand up in front of the webcam.
- Pinch your **thumb** and **index finger** together or apart to adjust brightness.
- Press **`q`** to quit.

---

## 🎮 Controls

| Gesture | Action |
|---------|--------|
| Thumb + Index close together | Minimum brightness |
| Thumb + Index spread apart | Maximum brightness |
| Press `q` | Quit the application |

---

## 🔧 Customization

In `handtip_detect_brightness_control.py`, the mapping range can be adjusted:

```python
# Change [2, 250] to match the distance range comfortable for your hand/camera
brightness = np.interp(length, [2, 250], [0, 100])
```

- Increase the upper bound (e.g., `300`) if you need to stretch your fingers more.
- Decrease the lower bound if the minimum isn't triggering at pinch.

---

## 📦 Dependencies

| Library | Purpose |
|---------|---------|
| `opencv-python` | Webcam capture and drawing |
| `mediapipe` | Hand landmark detection |
| `screen-brightness-control` | Cross-platform brightness API |
| `numpy` | Distance-to-brightness interpolation |
| `pyttsx3` | Text-to-speech startup message |
| `pycaw` | Windows audio volume control (optional) |

---

## 📄 License

MIT License — feel free to use, modify, and share.
