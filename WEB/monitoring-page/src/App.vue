<template>
  <div class="container">
    <header class="header">
      <h2>헤더 제목</h2>
    </header>
    <div class="content">
      <div class="left-column">
        <div class="text-select-pair" v-for="(pair, index) in textSelectPairs" :key="index">
          <span class="select-label">선택:</span>
          <select v-model="pair.selectedOption">
            <option value="option1">옵션 1</option>
            <option value="option2">옵션 2</option>
            <option value="option3">옵션 3</option>
          </select>
        </div>
        <button @click="handleButtonClick">버튼</button>
      </div>
      <div class="video-box">
        <!-- 실시간 영상 송출을 위한 요소를 추가하세요 -->
      </div>
      <div class="right-column">
        <table>
          <thead>
            <tr>
              <th>헤더1</th>
              <th>헤더2</th>
              <th>헤더3</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data, index) in tableData" :key="index">
              <td>{{ data.item1 }}</td>
              <td>{{ data.item2 }}</td>
              <td>{{ data.item3 }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      textSelectPairs: [
        { selectedOption: '' },
        { selectedOption: '' },
        { selectedOption: '' }
      ],
      tableData: [
        { item1: '데이터1', item2: '데이터2', item3: '데이터3' },
        { item1: '데이터4', item2: '데이터5', item3: '데이터6' },
        { item1: '데이터7', item2: '데이터8', item3: '데이터9' }
      ]
    };
  },
  methods: {
    handleButtonClick() {
      // 버튼 클릭 이벤트 핸들러
    }
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #234377;
  font-family: 'Noto Sans KR', sans-serif;
}

.header {
  background-color: #395c6b;
  color: white;
  padding: 20px;
  text-align: center;
  margin-bottom: 20px;
}

.content {
  display: flex;
  align-items: flex-start;
}

.left-column {
  flex: 1;
  padding-right: 20px;
}

.text-select-pair {
  margin-bottom: 10px;
}

.select-label {
  margin-right: 10px;
}

button {
  display: block;
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #395c6b;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.video-box {
  flex: 1;
  padding: 20px;
  background-color: #ffffff;
  text-align: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.right-column {
  flex: 1;
  padding-left: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

th,
td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: center;
}

th {
  background-color: #395c6b;
  color: white;
}
</style>
