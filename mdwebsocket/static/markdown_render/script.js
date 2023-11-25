var vm = new Vue({
  el: '#root',
  data: {
    mdRaw: '',
    mdRawRender: ''
  },
  watch: {
    mdRaw: function(){
      this.mdRender()
    }
  },
  created() {
    this.mdRaw =document.getElementById("editor").value;
  },
  methods: {
    mdRender: function() {
      this.mdRawRender = marked(this.mdRaw);
    }
  }
})


