import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.134.0/build/three.module.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.134.0/examples/jsm/loaders/GLTFLoader.js';

export function setupThree(canvas) {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, 1280 / 720, 0.1, 1000);
  camera.position.z = 5;
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true });
  renderer.setSize(1280, 720);

  // Load 3D model (GLTF/GLB)
  let hat = null;
  const loader = new GLTFLoader();
  loader.load(
    './assets/low_poly_hat/scene.gltf', // Đường dẫn tới model
    (gltf) => {
      hat = gltf.scene;
      hat.scale.set(0.8, 0.8, 0.8); // Điều chỉnh scale nếu cần
      scene.add(hat);
    },
    undefined,
    (error) => {
      console.error('Error loading 3D model:', error);
    }
  );

  const light = new THREE.AmbientLight(0xffffff);
  scene.add(light);

  return { scene, camera, renderer, hatRef: () => hat };
}

export function updateHatPosition(hat, forehead) {
  if (!hat) return;
  const x = forehead.x * 1280;
  const y = forehead.y * 720;
  const z = forehead.z * 1000;

  const threeX = (x - 640) / 1280 * 5;
  const threeY = -(y - 360) / 720 * 5;
  const threeZ = -z / 100;

  hat.position.set(threeX, threeY + 0.5, threeZ); // +0.5 để đội lên trán
  hat.rotation.set(0, 0, 0); // Có thể chỉnh lại nếu cần
}

export function renderScene(renderer, scene, camera) {
  renderer.render(scene, camera);
}
