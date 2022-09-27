checkbox = document.querySelector('input[name="image-clear"]')
if (checkbox){
    checkbox.classList.add("form-check-input")
}

inputs = document.querySelectorAll('input');
select= document.querySelector('select')
for (var i = 0; i < inputs.length; i++) {
    inputs[i].classList.add('form-control');
}
select.classList.add('form-control')

