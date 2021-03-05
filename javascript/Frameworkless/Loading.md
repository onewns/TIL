# Loading

```js
export default () => {
  return `
  <div class="loading-wrapper">
    <div id="loading" class="loading"></div>
  </div>
  `
}
```

```css
.loading-wrapper {
	text-align: center;
}

.loading {
	display: inline-block;
	width: 100px;
	height: 100px;
	background-image: url('https://image.flaticon.com/icons/png/512/190/190420.png');
	background-size: contain;
	animation: spin 2s linear infinite;
}
@keyframes spin {
	from {
		transform: rotate(0);
	}
	to {
		transform: rotate(360deg);
	}
}
```

