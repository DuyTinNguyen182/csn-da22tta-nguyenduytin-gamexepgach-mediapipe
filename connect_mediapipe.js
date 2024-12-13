const socket = new WebSocket('ws://127.0.0.1:12345');

socket.onopen = () => {
  console.log('Connected to WebSocket server');
};
const MPcanvas = document.getElementById('videoCanvas');
const MPctx = MPcanvas.getContext('2d');

MPcanvas.width = 400;
MPcanvas.height = 300;
// const socket = new WebSocket('ws://127.0.0.1:12345');

socket.onmessage = (event) => {
  const message = JSON.parse(event.data);

  if (message.type === 'frame') {
    const image = new Image();
    image.onload = () => {
      MPctx.drawImage(image, 0, 0, MPcanvas.width, MPcanvas.height);
    };
    image.src = `data:image/jpeg;base64,${message.data}`;
  } else if (message.type === 'command') {
    const command = message.data;
    console.log(`Received command: ${command}`);
    if (!board.gameOver && board.isPlaying && !isPaused) {
      switch (command) {
        case 'LEFT':
          brick.moveLeft();
          break;
        case 'RIGHT':
          brick.moveRight();
          break;
        case 'DOWN':
          brick.moveDown();
          break;
        case 'UP':
          brick.rotate();
          break;
        // default:
        //   break;
      }
    }
  }
};

// socket.onmessage = (event) => {
//   const command = event.data;
//   console.log(`Received command: ${command}`);  // Log lệnh nhận được
//   if (!board.gameOver && board.isPlaying && !isPaused) {
//     switch (command) {
//       case 'LEFT':
//         brick.moveLeft();
//         break;
//       case 'RIGHT':
//         brick.moveRight();
//         break;
//       case 'DOWN':
//         brick.moveDown();
//         break;
//       case 'UP':
//         brick.rotate();
//         break;
//       default:
//         break;
//     }
//   }
// };

socket.onclose = () => {
  console.log('Disconnected from WebSocket server');
};