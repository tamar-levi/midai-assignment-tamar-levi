**MID AI – Take Home Assignment (AI Intern)**

The YOLO-annotated image or video file.

A specifications.json file generated from a document using an LLM.

part1.txt, part2.txt, part3.txt – Each file includes:

3–5 bullet points explaining my steps.

A brief summary (2–4 sentences) of my approach and any challenges faced.

README.md – This file. Includes Docker build and run instructions.


🐳 Docker Instructions
To reproduce the tasks in a clean Docker environment:

1. Clone the repository
git clone https://github.com/tamar-levi/midai-assignment-tamar-levi.git
cd midai-assignment-tamar-levi

2. Build the Docker image
3. docker build -t midai-assignment .

3. Run the Docker container
4. docker run --rm -it --name midai-container midai-assignment


⚙️ Requirements & Tools
The project uses the following main tools and libraries:

Python 3.10

PyTorch

OpenCV

YOLOv5

ffmpeg

Git

NetFree CA Certificates for secure HTTP access

All dependencies are listed in requirements.txt and are installed during Docker build.

