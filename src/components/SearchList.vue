<template>
    <div>
        <div class="test">
         <q-input filled bottom-slots v-model="text" maxlength="24" :dense="dense">

        <template v-slot:append>
          <q-icon v-if="text !== ''" name="close" @click="text = ''" class="cursor-pointer" />
          <q-icon name="search" />
        </template>
      </q-input>
      </div>
      <q-separator color="blue-grey-9" />
    </div>
</template>