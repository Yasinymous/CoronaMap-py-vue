<template>
  <div class="q-pa-md">
    <q-table
      class="my-sticky-header-column-table"
      title="24-30 Nisan 2021"
      :data.sync="data"
      :columns="columns"
      row-key="name"
      :hide-pagination="true"
      :rows-per-page-options="[0]"
      dense/>
  <div>
</div>
  </div>
</template>

<script>
export default {
    name:'WeekList',
    props: {
    cities: { type: Array, required: true }
    
 },
  data () {
    return {
      columns: [
        {
          name: 'name',
          required: true,
          label: 'İl Adı',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
        },
        {
          name: 'vaka',
          align: 'center',
          label: 'Sayı',
          field: 'vaka',
          sortable: true
        }
      ],
      data: this.cities
    }
  }
}
</script>

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

