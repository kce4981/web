<script lang="ts">
    export let textContent: string = '';
    export let author: string = '';
    import Paper, { Title, Content } from '@smui/paper';
    
    const paperSty: string = 'width:80%;';
    const titleSty: string = 'vertical-align:super;';
    const contentSty: string = 'margin:2em';

    author = author.charAt(0).toUpperCase() + author.slice(1);
</script>


<Paper style={paperSty}>
    <Title style={titleSty}>
        <span class="material-symbols-outlined">person</span>
        {author}
    </Title>
    <Content style={contentSty}>{textContent}</Content>
</Paper>

<style>

.material-symbols-outlined {
    /* Is there better ways ? */
    vertical-align: -0.15em;
}

</style>