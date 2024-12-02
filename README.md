# HandSolve AI

HandSolve AI is an innovative application that combines computer vision, hand gesture recognition, and artificial intelligence to solve mathematical problems in real-time. This project showcases the power of integrating multiple cutting-edge technologies to create an interactive and educational tool.

## Key Features

- **Real-time Hand Tracking**: Utilizes the cvzone HandTrackingModule to accurately detect and track hand movements.
- **Dynamic Drawing Canvas**: Allows users to draw mathematical problems using hand gestures.
- **AI-Powered Problem Solving**: Leverages Google's Generative AI (Gemini model) to interpret and solve the drawn mathematical problems.
- **Interactive User Interface**: Built with Streamlit, providing a seamless and responsive user experience.
- **Live Video Feed**: Incorporates OpenCV for real-time video capture and processing.

## Technologies Used

- Python
- OpenCV (cv2)
- cvzone
- Google Generative AI
- Streamlit
- NumPy
- Pillow (PIL)

## How It Works

1. The application captures video input from the user's camera.
2. Hand gestures are detected and tracked in real-time.
3. Users can draw on a virtual canvas using specific hand gestures.
4. Once the mathematical problem is drawn, another gesture triggers the AI analysis.
5. The AI interprets the drawn problem and provides a solution.
6. Results are displayed in real-time on the user interface.

This project demonstrates the potential of combining computer vision, gesture recognition, and AI to create interactive educational tools. It's an excellent example of how technology can make learning more engaging and accessible.