import { VRButton } from 'three/examples/jsm/webxr/VRButton.js';

const scene  = new THREE.Scene(); // what and where is being rendered
const camera = new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight, 0.1,1000); //(camera deg, AR, near plane(too close wont be displayed), far plane(too far wont be displayed))  

var renderer = new THREE.WebGLRenderer({antialias: true});// antialias to make result not as jagged

renderer.setSize(window.innerWidth,window.innerHeight);
renderer.setClearColor("#e5e5e5"); // set background colour(via HEX)

//render into html doc: 
document.body.appendChild(renderer.domElement);
/*
// create VR access: 
document.body.appendChild(VRButton.createButton(renderer));
renderer.xr.enabled = true;

renderer.setAnimationLoop(function () {

    renderer.render(scene, camera);

});
*/
