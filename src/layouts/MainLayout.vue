<template>
  <q-layout view="hHh lpR fff">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar >
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.iconscout.com/icon/free/png-256/stop-coronavirus-2332166-1938991.png">
          </q-avatar>
          Corona Map
        </q-toolbar-title>
       <q-btn dense flat round icon="menu" @click="right = !right" />
      </q-toolbar>
      <!--
        <q-tabs dense align="left">
        <q-route-tab to="/page2" label="Anasayfa" />
        <q-route-tab to="/page1" label="Genel Koronavirüs Tablosu" />
      </q-tabs>
      -->
    </q-header>

    <q-drawer show-if-above v-model="right" side="right" bordered>
      <WeekList :cities="cities" />
       <q-separator color="blue-grey-9" />
      <CityDetails />
    </q-drawer>

    <q-page-container>
      <Map />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.iconscout.com/icon/free/png-256/stop-coronavirus-2332166-1938991.png">
          </q-avatar>
         Corona Map{{ test }}
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
import WeekList from 'components/WeekList'
import Map from 'components/Map'
import CityDetails from 'components/CityDetails'
import firebase from 'boot/firebase'
let ref = firebase.firestore().collection('cities').orderBy('id', 'asc')
export default {
  name: 'MainLayout',
  data () {
    return {
      right: false,
      cities: [],
      errors: [],
      dense: true,
      text: '',
      ph: '',
    }
  },
  components: {
    WeekList,
    Map,
    CityDetails,
  },
  created () {
    ref.onSnapshot((querySnapshot) => {
      this.cities = [];
      querySnapshot.forEach((doc) => {
        this.cities.push({
          id: doc.data().id,
          name: doc.data().name,
          vaka: doc.data().vaka,
          date: doc.data().date
        });
      });
    });
  },  
}
</script>

<style>
.test{
  margin-left: 15px;
  margin-right: 15px;
  margin-top: 12px;
}
.nav-item{
  padding-right: 50px;

}
@media only screen and (max-width: 500px){
   .nav-item{
     font-size: 15px;
   }
}
</style>
