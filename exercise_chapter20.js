const post = { id: 1, title: "Hello", image: null};
const {title} = post;
console.log(title, post.autor?.email?? "Unknow");