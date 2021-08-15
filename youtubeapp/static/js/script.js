// console.log("attached")
const drop = document.getElementById("drop");
const dropdown = document.getElementsByClassName('dropdown')[0]
console.log(dropdown)
console.log(drop)
drop.onclick = () =>{
    if(dropdown.style.display === "none"){
    dropdown.style.display = "block";
    }
    else{
        dropdown.style.display = "none";
    }
}