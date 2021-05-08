<template>
<div>
  <div class="title">
      <h4 class="title-font">{{ MapGetCity[0].name }}</h4>
 </div>
  <div class="table-size q-pa-md">
 
    <q-table
      :data.sync="MapGetCity"
      :columns="columns"
      row-key="name"
       :hide-pagination="true"
      :rows-per-page-options="[0]"
      dense
      no-data-label="Veriler Bulunamadı..." 
    />
  </div>
  </div>
</template>

<script>

export default {
    name:'CityDetails',
     props: {
    MapGetCity: { type: Array, required: true }   
  },
  data () {
    return {   
      columns: [
        {
          name: 'date',
          required: true,
          label: 'Tarih',
          align: 'left',
          field: row => row.date,
          format: val => `${val}`,
        },
        { name: 'vaka', align: 'center', label: 'Sayı', field: 'vaka' },

      ],
        data: this.MapGetCity,
    }  
  },
}

</script>
<style>
.title-font{
  padding: 0px;
  margin: 0px;
}
.table-size{
  text-align: justify;
  max-width: 600px;
  margin: auto;
}
@media only screen and (max-width: 800px){
    .title .title-font{
        font-size: 20px;
    }
 }

</style>
<style lang="sass">
.my-sticky-header-column-table
  /* height or max-height is important */
  height: 265px

  /* specifying max-width so the example can
    highlight the sticky column on any browser window */
  max-width: 600px

  td:first-child
    /* bg color is important for td; just specify one */
    background-color: #cfd8dc !important

  tr th
    position: sticky
    /* higher than z-index for td below */
    z-index: 2
    /* bg color is important; just specify one */
    background: #fff

  /* this will be the loading indicator */
  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
    /* highest z-index */
    z-index: 3
  thead tr:first-child th
    top: 0
    z-index: 1
  tr:first-child th:first-child
    /* highest z-index */
    z-index: 3

  td:first-child
    z-index: 1

  td:first-child, th:first-child
    position: sticky
    left: 0
</style>

