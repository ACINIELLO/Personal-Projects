//import VRButton.js

const scene  = new THREE.Scene(); // what and where is being rendered
const camera = new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight, 0.1,1000); //(camera deg, AR, near plane(too close wont be displayed), far plane(too far wont be displayed))  

var renderer = new THREE.WebGLRenderer({antialias: true});// antialias to make result not as jagged

renderer.setSize(window.innerWidth,window.innerHeight);
renderer.setClearColor("#e5e5e5"); // set background colour(via HEX)

//render into html doc: 
document.body.appendChild(renderer.domElement);

// include a box geometry:

const boxWidth = 1;
const boxHeight = 1;
const boxDepth = 1;
const geometry = new THREE.BoxGeometry(boxWidth, boxHeight, boxDepth);
const material = new THREE.MeshBasicMaterial({color: 0x44aa88});
const cube = new THREE.Mesh(geometry, material); // takes in geometry and material/colour to create the cube(which is the "cubes mesh")

cube.position.y =1;
scene.add(cube);







// create VR access: 
//document.body.appendChild(VRButton.createButton(renderer));
//renderer.xr.enabled = true;

//animate:
/*
renderer.setAnimationLoop(function () {
    

    renderer.render(scene, camera);

});
*/



//add some light:
var light = new THREE.PointLight(0xFFFFFF,10,500); // (colour, intensity,range/distance)
light.position.set(0,0,25);
scene.add(light);

//reposition camera so that we can see objects (as default = inside object):


camera.position.x = 5; 
renderer.render(scene,camera);

function animate()
{
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01; 
 
    renderer.render(scene,camera);
    
}


//call function to run:

animate();




