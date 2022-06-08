<script lang="ts">
import BlogPost from "./lib/blogPost.svelte";
import Libs from "./lib/libs.svelte";
</script>

<Libs/>
<div class="app">
    <div class="leftToolBar"></div>
    <div class="Post">
        <BlogPost textContent='aaaa'/>
        <BlogPost textContent='aaaa'/>
        <BlogPost textContent='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi diam est, pellentesque ut mollis eu, aliquam a est. Fusce rutrum commodo ante sed mattis. Aenean ultrices, nulla vitae sagittis tincidunt, est urna pellentesque tellus, pulvinar scelerisque lacus ipsum eget nibh. Nullam congue, eros vel dapibus vestibulum, leo odio tincidunt dolor, vel blandit sapien ligula id lacus. Nam in tellus bibendum lorem ullamcorper dictum. Praesent vitae porttitor dolor, nec bibendum ex. Integer tristique, neque in elementum ullamcorper, neque mi mattis nisl, vel placerat dolor lorem imperdiet dolor. Fusce ipsum velit, imperdiet sed lacus at, blandit luctus orci. Curabitur rutrum mattis magna fermentum mattis. Proin placerat, elit vel viverra facilisis, augue urna tempus diam, id sagittis massa quam sed justo. Praesent ut facilisis augue. Cras mattis metus at velit mattis, vel condimentum urna vulputate. '/>
        <BlogPost textContent='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi diam est, pellentesque ut mollis eu, aliquam a est. Fusce rutrum commodo ante sed mattis. Aenean ultrices, nulla vitae sagittis tincidunt, est urna pellentesque tellus, pulvinar scelerisque lacus ipsum eget nibh. Nullam congue, eros vel dapibus vestibulum, leo odio tincidunt dolor, vel blandit sapien ligula id lacus. Nam in tellus bibendum lorem ullamcorper dictum. Praesent vitae porttitor dolor, nec bibendum ex. Integer tristique, neque in elementum ullamcorper, neque mi mattis nisl, vel placerat dolor lorem imperdiet dolor. Fusce ipsum velit, imperdiet sed lacus at, blandit luctus orci. Curabitur rutrum mattis magna fermentum mattis. Proin placerat, elit vel viverra facilisis, augue urna tempus diam, id sagittis massa quam sed justo. Praesent ut facilisis augue. Cras mattis metus at velit mattis, vel condimentum urna vulputate. '/>
        <BlogPost author='我是捷克' textContent='我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞我喜歡愛蜜莉亞喜歡愛蜜莉亞喜歡愛蜜莉亞'/>
        <BlogPost author='pekora' textContent='Hello world'/>
    </div>
</div>

<style>
div.Post {
    display: flex;
    flex-direction: column-reverse;
    align-items: center;
    gap: 1em;
    width: 50%;
    height: 100%;
    background-color: darkgray;
}

div.app {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
}

</style>