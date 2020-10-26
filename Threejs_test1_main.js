//import VRButton.js
var camera,scene,renderer,cube; // globalize variables 
function initialize() {
	// Init scene
	scene = new THREE.Scene();

	// Init camera (PerspectiveCamera)
	camera = new THREE.PerspectiveCamera(
		75,
		window.innerWidth / window.innerHeight,
		0.1,
		1000
	);

	// Init renderer
	renderer = new THREE.WebGLRenderer({ antialias: true });

	// Set size (whole window)
	renderer.setSize(window.innerWidth, window.innerHeight);

	// Render to canvas element
	document.body.appendChild(renderer.domElement);
    //reposition camera so that we can see objects (as default = inside object):


    camera.position.x = 5; 
    
    //add some light:
    var light = new THREE.PointLight(0xFFFFFF,5,500); // (colour, intensity,range/distance)
    light.position.set(10,0,25);
    scene.add(light);

    



    
// include a box geometry:

const boxWidth = 1;
const boxHeight = 1;
const boxDepth = 1;
const geometry = new THREE.BoxGeometry(boxWidth, boxHeight, boxDepth);
const material = new THREE.MeshBasicMaterial({color: 0x44aa88});
const cube = new THREE.Mesh(geometry, material); // takes in geometry and material/colour to create the cube(which is the "cubes mesh")

cube.position.y =1;
scene.add(cube);

}




// create VR access: 
//document.body.appendChild(VRButton.createButton(renderer));
//renderer.xr.enabled = true;

//animate:
/*
renderer.setAnimationLoop(function () {
    

    renderer.render(scene, camera);

});
*/




//renderer.render(scene,camera);

function animate()
{
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01; 
     cube.rotation.y += 0.01; 
     cube.rotation.z += 0.01; 

    renderer.render(scene,camera);
    
}


//call function to run:
initialize();
animate();




