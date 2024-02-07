let reg_form = document.getElementById('registration')

reg_form.onsubmit = (e) => {
  e.preventDefault();
  var form = new FormData(reg_form);
  fetch("http://localhost:5000/user/create", { method :'POST', body : form})
            .then( response => response.json() )
            .then( data => {
              console.log(data)
              console.log(data.success)
              if(data.success){
                console.log(data.user_id)
                window.location.href = `/user/home/${data.user_id}`
              }
              else{
                console.log(data.reg_errors)
                let currentErrorList = document.getElementById('reg_error_list')
                let alternateErrorList = document.getElementById('login_error_list')
                currentErrorList.innerHTML = data.reg_errors
                alternateErrorList.innerHTML = ''
              }
        });
};