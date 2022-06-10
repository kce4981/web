<script lang="ts">
import Libs from "./lib/libs.svelte";
import RenderBlog from "./RenderBlog.svelte";
import ToolBar from "./ToolBar.svelte";

</script>

<Libs/>
<ToolBar/>
<div></div>
<div class="app">
    <div class="leftToolBar"></div>
    <RenderBlog/>
</div>

<style>

div.app {
    margin-top:1em;
    width: 100%;
    height: auto;
    display: flex;
    justify-content: center;
}

</style>