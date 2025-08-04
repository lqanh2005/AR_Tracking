export function setupCamera(videoElement, onFrameCallback) {
  const cameraFeed = new Camera(videoElement, {
    onFrame: onFrameCallback,
    width: 1280,
    height: 720
  });
  cameraFeed.start();
}
