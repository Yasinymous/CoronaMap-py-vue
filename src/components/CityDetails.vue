<template>
  <div class="q-pa-md">
    <q-markup-table flat bordered>
      <thead class="bg-white">
        <tr>
          <th colspan="5">
            <div class="row no-wrap items-center">
              <q-img
                style="width: 70px"
                :ratio="1"
                class="rounded-borders"
                src="https://upload.wikimedia.org/wikipedia/commons/8/83/Adana_city.png"
              />

              <div class="text-h4 q-ml-md text-black">Adana</div>
            </div>
          </th>
        </tr>
        <tr>
          <th class="text-left">Detaylar</th>
          <th class="text-right"></th>
        </tr>
      </thead>
      <tbody class="bg-blue-grey-11">
        <tr>
          <td class="text-left">Vaka Sayısı</td>
          <td class="text-right">192,54</td>
        </tr>
      </tbody>
    </q-markup-table>
  </div>
</template>

<script>
export default {
    name:'CityDetails',
}
</script>
