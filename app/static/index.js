
    






fetch('./api/timeline_post')
   .then(response => response.json())
   .then( data => console.log(data) & display(data.timelineposts));



display = data => {
  console.log(data)
  const dataDiv = document.getElementById('entries')
  data.forEach(element => {
    const Element = document.createElement('p');
    Element.innerText = 'Date: ' + element.created_at + '\xa0\xa0\xa0\xa0\xa0\xa0\xa0' + 'Name: ' + element.name + '\xa0\xa0\xa0\xa0\xa0\xa0\xa0'+ 'Email: ' + element.email + '\xa0\xa0\xa0\xa0\xa0\xa0\xa0' + 'Content: '+ element.content
    dataDiv.append(Element);
  })
}

update = data => {
  console.log(data)
  const dataDiv = document.getElementById('entries')
  const element = data[0]
  const Updates = document.createElement('p');
  Updates.innerText = 'Date:' + element.created_at + '\xa0\xa0\xa0\xa0\xa0\xa0\xa0' + 'Name:' + element.name + '\xa0\xa0\xa0\xa0\xa0\xa0\xa0'+ 'Email:' + element.email + '\xa0\xa0\xa0\xa0\xa0\xa0\xa0' + 'Content:'+ element.content
  dataDiv.prepend(Updates);
  
}


form = document.getElementById('form');
 
    form.addEventListener('submit', function(e) {
    // Prevent default behavior:
    e.preventDefault();
    // Create payload as new FormData object:
    const payload = new FormData(form);
    // Post the payload using Fetch:
    fetch('./api/timeline_post', {
    method: 'POST',
    body: payload,
    })
    .then(res => res.json())
    .then(data => fetch('./api/timeline_post') )
   .then(response => response.json())
   .then( data =>  update(data.timelineposts))
   const inputs = document.querySelectorAll('#name, #content, #email');

  inputs.forEach(input => {
    input.value = '';
  });
    

})



   




   //.then(data => data.forEach(char => console.log(char)))
   

 