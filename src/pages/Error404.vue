<template>
  <div class="fullscreen bg-red text-white text-center q-pa-md flex flex-center">
    <div>

      <div>
        <img src="https://yasinymous.com/images/mainlogo/mainbeyaz.svg" alt="" width="100">
      </div>

      <div style="font-size: 30vh">
        404
      </div>

      <q-btn
        class="q-mt-xl"
        color="white"
        text-color="red"
        unelevated
        to="/"
        label="Anasayfaya Dön"
        no-caps
      />

    </div>
  </div>
</template>

<script>
export default {
  name: 'Error404'
}
</script>
