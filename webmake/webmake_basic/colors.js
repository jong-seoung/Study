
function nightdayhandeler(self) {
  var target = document.querySelector('body')
  var target3 = document.querySelectorAll('a')
  console.log(target3)
  if(self.value === '다크모드ON')
  {
  target.style.background = 'black';
  target.style.color = 'white';

  target3.forEach(d => d.style.color = 'white');
  self.value = '다크모드OFF';
  }
  else
  {
  target.style.background = 'white';
  target.style.color = 'black';

  target3.forEach(d => d.style.color = 'black');
  self.value = '다크모드ON';
  }
  }
