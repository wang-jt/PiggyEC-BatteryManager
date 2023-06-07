XMLHttpRequest
export function reqAPI(type, addr, data) {
    if(type != 'POST') type = 'GET';
    const xhr = new XMLHttpRequest();
    xhr.open(type, 'http://localhost:5555' + addr, false);
    xhr.send(JSON.stringify(data));
    if (xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      return data;
    } else {
      console.log('Error:', xhr.status);
    }
}  